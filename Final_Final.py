import os
import re
import json
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key
from pynput import keyboard
from pynput.mouse import Listener as MouseListener
import time
import mss
import datetime

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

def generate_filename():
    files = os.listdir(folder_path)
    log_numbers = [int(re.findall(r'log_(\d+).json', file)[0]) for file in files if re.match(r'log_\d+.json', file)]
    new_log_number = max(log_numbers) + 1 if log_numbers else 1
    return f'log_{new_log_number}.json'

def on_click(x, y, button, pressed):
    global event_counter, start_time
    event_counter += 1
    timestamp = round(time.perf_counter() - start_time, 4)
    data["data"].append({"event_id": event_counter, "x": round(x, 4), "y": round(y, 4), "button": str(button), "type": "click", "timestamp": timestamp, "UserId": UserId})

def on_move(x, y):
    global event_counter, start_time, last_recorded_time, last_v, last_t_v, last_x, last_y
    current_time = time.perf_counter()
    
    # Check if at least 0.1 seconds have passed since last recorded mouse movement
    if current_time - last_recorded_time >= 0.025:
        event_counter += 1
        timestamp = round(current_time - start_time, 4)
        delta_t = current_time - last_t_v
        delta_x = x - last_x
        delta_y = y - last_y
        
        # distance is calculated as sqrt((delta_x)^2 + (delta_y)^2)
        distance = round((delta_x ** 2 + delta_y ** 2) ** 0.5, 4)
        
        # velocity is calculated as distance / delta_t
        velocity = round(distance / delta_t, 4) if delta_t != 0 else 0
        
        # acceleration is calculated as (v - last_v) / delta_t
        acceleration = round((velocity - last_v) / delta_t, 4) if delta_t != 0 else 0
        
        data["data"].append({
            "event_id": event_counter, 
            "x": round(x, 4), 
            "y": round(y, 4), 
            "distance": distance,
            "velocity": velocity,
            "acceleration": acceleration,
            "type": "move", 
            "timestamp": timestamp, 
            "UserId": UserId
        })
        
        # update values
        last_x, last_y = x, y
        last_v = velocity
        last_t_v = current_time
        last_recorded_time = current_time

def on_press(key):
    global stop_listener, event_counter, start_time
    press_time = time.perf_counter()
    if key not in current_pressed or (current_pressed[key]["is_released"] and round(press_time - current_pressed[key]["timestamp"], 4) > 0.05):
        #event_counter += 1
        timestamp = round(press_time - start_time, 4)
        # data["data"].append({"event_id": event_counter, "key": str(key), "type": "press", "timestamp": timestamp})
        if key == keyboard.Key.f10:
            stop_listener = True
        current_pressed[key] = {"timestamp": timestamp, "is_released": False, 'press_time': press_time}

def on_release(key):
    global event_counter, start_time
    if key in current_pressed and not current_pressed[key]["is_released"]:
        event_counter += 1
        release_time = time.perf_counter()
        press_time = current_pressed[key]['press_time']
        duration = round(release_time - press_time,4)
        timestamp = round(release_time - start_time, 4)
        data["data"].append({"event_id": event_counter, "key": str(key), "type": "release", "duration": duration ,"timestamp": timestamp, "UserId": UserId})
        current_pressed[key]["is_released"] = True
        current_pressed[key]["timestamp"] = timestamp

def capture_screenshot():
    global start_time
    current_time = time.perf_counter()
    timestamp = round(current_time - start_time, 4)
    with mss.mss() as sct:
        filename = sct.shot(mon=-1, output= r'C:\\Users\\is0482sf\\Desktop\\Data_Listener\\screenshot\\ss_{}.png'.format(str(timestamp).replace(".", "")))

def main():
    filename = generate_filename()

    with KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
        with MouseListener(on_click=on_click, on_move=on_move) as mouse_listener:
            while not stop_listener:
                capture_screenshot()
                time.sleep(1)

    with open(folder_path + filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    main()