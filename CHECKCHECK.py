import os
import re
import json
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key
from pynput import keyboard
from pynput.mouse import Listener as MouseListener
import time
import mss

folder_path = 'C:/Users/is0482sf/Desktop/Data_Listener/'
stop_listener = False
current_pressed = {}
data = {"data": []}
event_counter = 0
last_recorded_time = 0

# Record start time
start_time = time.perf_counter()

last_x, last_y = 0, 0
last_v = 0
last_t_v = time.perf_counter()
UserId = 0

last_keyboard_event = None

def generate_filename():
    files = os.listdir(folder_path)
    log_numbers = [int(re.findall(r'log_(\d+).json', file)[0]) for file in files if re.match(r'log_\d+.json', file)]
    new_log_number = max(log_numbers) + 1 if log_numbers else 1
    return f'log_{new_log_number}.json'

def on_click(x, y, button, pressed):
    global event_counter, start_time, last_keyboard_event
    event_counter += 1
    timestamp = round(time.perf_counter() - start_time, 5)
    # Combine the mouse and keyboard events
    combined_event = {
        "event_id": event_counter,
        "x": round(x, 5),
        "y": round(y, 5),
        "button": str(button),
        "type": "click",
        "timestamp": timestamp,
        "UserId": UserId,
        "keyboard": last_keyboard_event if last_keyboard_event else "null",
    }
    data["data"].append(combined_event)
    # reset the keyboard event
    last_keyboard_event = None

def on_move(x, y):
    global event_counter, start_time, last_recorded_time, last_v, last_t_v, last_x, last_y, last_keyboard_event
    
    current_time = time.perf_counter()
    
    if current_time - last_recorded_time >= 0.025:
        event_counter += 1
        timestamp = round(current_time - start_time, 5)
        delta_t = current_time - last_t_v
        delta_x = x - last_x
        delta_y = y - last_y
        
        # distance is calculated as sqrt((delta_x)^2 + (delta_y)^2)
        # velocity is calculated as distance / delta_t
        # acceleration is calculated as (v - last_v) / delta_t

        distance = round((delta_x ** 2 + delta_y ** 2) ** 0.5, 5)
        velocity = round(distance / delta_t, 5) if delta_t != 0 else 0
        acceleration = round((velocity - last_v) / delta_t, 5) if delta_t != 0 else 0
        
        event_data = {
            "event_id": event_counter, 
            "x": round(x, 5), 
            "y": round(y, 5), 
            "distance": distance,
            "velocity": velocity,
            "acceleration": acceleration,
            "type": "move", 
            "timestamp": timestamp, 
            "UserId": UserId,
            "keyboard": last_keyboard_event if last_keyboard_event else "null",
        }
        data["data"].append(event_data)
    
        # reset the keyboard event
        last_keyboard_event = None
      
        # update values
        last_x, last_y = x, y
        last_v = velocity
        last_t_v = current_time
        last_recorded_time = current_time

def on_press(key):
    global stop_listener, start_time, last_keyboard_event
    press_time = time.perf_counter()
    timestamp = round(press_time - start_time, 5)
    if key == keyboard.Key.f10:
        stop_listener = True
    current_pressed[key] = {"timestamp": timestamp, "is_released": False, 'press_time': press_time}

def on_release(key):
    global event_counter, start_time, last_keyboard_event
    if key in current_pressed and not current_pressed[key]["is_released"]:
        release_time = time.perf_counter()
        press_time = current_pressed[key]['press_time']
        duration = round(release_time - press_time,5)
        timestamp = round(release_time - start_time, 5)
        
        # store the release event instead of writing it to the log
        last_keyboard_event = {"key": str(key), "type": "release", "duration": duration}
        current_pressed[key]["is_released"] = True

def capture_screenshot():
    global start_time
    current_time = time.perf_counter()
    timestamp = round(current_time - start_time, 5)
    directory = r'C:\\Users\\is0482sf\\Desktop\\Data_Listener\\screenshot\\'
    filename = 'ss_{}.png'.format(str(timestamp).replace(".", "_"))
    full_path = os.path.join(directory, filename)

    # Check if the directory exists and if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
    with mss.mss() as sct:
        try:
            filename = sct.shot(mon=-1, output=full_path)
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    filename = generate_filename()

    with KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
        with MouseListener(on_click=on_click, on_move=on_move) as mouse_listener:
            while not stop_listener:
                capture_screenshot()
                time.sleep(0.5)

    with open(folder_path + filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    main()