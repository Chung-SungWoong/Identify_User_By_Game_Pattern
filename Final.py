import os
import re
import json
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key
from pynput import keyboard
from pynput.mouse import Listener as MouseListener
import time

folder_path = 'C:/Users/is0482sf/Desktop/Data_Listener/'
stop_listener = False
current_pressed = {}
data = {"data": []}
event_counter = 0
last_recorded_time = 0

# Record start time
start_time = time.perf_counter()

# If not working Erase it
last_x, last_y = 0, 0
last_v = 0
last_t_v = time.perf_counter()

def generate_filename():
    files = os.listdir(folder_path)
    log_numbers = [int(re.findall(r'log_(\d+).json', file)[0]) for file in files if re.match(r'log_\d+.json', file)]
    new_log_number = max(log_numbers) + 1 if log_numbers else 1
    return f'log_{new_log_number}.json'

def on_click(x, y, button, pressed):
    global event_counter, start_time
    event_counter += 1
    timestamp = round(time.perf_counter() - start_time, 3)
    data["data"].append({"event_id": event_counter, "x": round(x, 3), "y": round(y, 3), "button": str(button), "pressed": pressed, "type": "click", "timestamp": timestamp})

"""
def on_move(x, y):
    global event_counter, start_time, last_recorded_time
    current_time = time.perf_counter()
    # Check if at least 0.1 seconds have passed since last recorded mouse movement
    if current_time - last_recorded_time >= 0.03:
        event_counter += 1
        timestamp = round(current_time - start_time, 3)
        data["data"].append({"event_id": event_counter, "x": round(x, 3), "y": round(y, 3), "type": "move", "timestamp": timestamp})
        last_recorded_time = current_time  # update last_recorded_time
"""

def on_move(x, y):
    global event_counter, start_time, last_recorded_time, last_v, last_t_v, last_x, last_y
    current_time = time.perf_counter()
    
    # Check if at least 0.1 seconds have passed since last recorded mouse movement
    if current_time - last_recorded_time >= 0.03:
        event_counter += 1
        timestamp = round(current_time - start_time, 3)
        delta_t = current_time - last_t_v
        delta_x = x - last_x
        delta_y = y - last_y
        
        # velocity is calculated as sqrt((delta_x)^2 + (delta_y)^2) / delta_t
        velocity = round((delta_x ** 2 + delta_y ** 2) ** 0.5 / delta_t, 3) if delta_t != 0 else 0
        
        # acceleration is calculated as (v - last_v) / delta_t
        acceleration = round((velocity - last_v) / delta_t, 3) if delta_t != 0 else 0
        
        data["data"].append({
            "event_id": event_counter, 
            "x": round(x, 3), 
            "y": round(y, 3), 
            "velocity": velocity,
            "acceleration": acceleration,
            "type": "move", 
            "timestamp": timestamp
        })
        
        # update values
        last_x, last_y = x, y
        last_v = velocity
        last_t_v = current_time
        last_recorded_time = current_time  

def on_press(key):
    global stop_listener, event_counter, start_time
    if key not in current_pressed or (current_pressed[key]["is_released"] and round(time.perf_counter() - current_pressed[key]["timestamp"], 3) > 0.05):
        event_counter += 1
        timestamp = round(time.perf_counter() - start_time, 3)
        data["data"].append({"event_id": event_counter, "key": str(key), "type": "press", "timestamp": timestamp})
        if key == keyboard.Key.f10:
            stop_listener = True
        current_pressed[key] = {"timestamp": timestamp, "is_released": False}

def on_release(key):
    global event_counter, start_time
    if key in current_pressed and not current_pressed[key]["is_released"]:
        event_counter += 1
        release_time = time.perf_counter()
        press_time = current_pressed[key]['press_time']
        duration = release_time - press_time
        timestamp = round(time.perf_counter() - start_time, 3)
        data["data"].append({"event_id": event_counter, "key": str(key), "type": "release", "duration": duration ,"timestamp": timestamp})
        current_pressed[key]["is_released"] = True
        current_pressed[key]["timestamp"] = timestamp

def main():
    filename = generate_filename()

    with KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
        with MouseListener(on_click=on_click, on_move=on_move) as mouse_listener:
            while not stop_listener:
                time.sleep(1)

    with open(folder_path + filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    main()
