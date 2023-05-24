import os
import re
import json
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key
from pynput import keyboard
import pyautogui
import time

# Global Variables
folder_path = '/Users/chung_sungwoong/Desktop/Practice/Identify_User_By_Game_Pattern/'
stop_listener = False
last_x, last_y, last_t = None, None, None
current_pressed = {}
data = {"data": []}
event_counter = 0

# Generate log filename
def generate_filename():
    files = os.listdir(folder_path)
    log_numbers = [int(re.findall(r'log_(\d+).json', file)[0]) for file in files if re.match(r'log_\d+.json', file)]
    new_log_number = max(log_numbers) + 1 if log_numbers else 1
    return f'log_{new_log_number}.json'

# Mouse clicked
def on_click(x, y, button, pressed):
    global event_counter
    event_counter += 1
    data["data"].append({"event_id": event_counter, "x": int(x), "y": int(y), "button": str(button), "pressed": pressed, "type": "click"})

# Keyboard pressed
def on_press(key):
    global stop_listener, event_counter
    if key not in current_pressed or (current_pressed[key]["is_released"] and time.perf_counter() - current_pressed[key]["release_time"] > 0.05):
        event_counter += 1
        press_time = time.perf_counter()
        data["data"].append({"event_id": event_counter, "key": str(key), "type": "press", "press_time": press_time})
        if key == keyboard.Key.esc:
            stop_listener = True
        current_pressed[key] = {"press_time": press_time, "is_released": False}

# Keyboard released
def on_release(key):
    global event_counter
    if key in current_pressed and not current_pressed[key]["is_released"]:
        event_counter += 1
        release_time = time.perf_counter()
        data["data"].append({"event_id": event_counter, "key": str(key), "type": "release", "release_time": release_time})
        press_time = current_pressed[key]['press_time']
        duration = release_time - press_time
        data["data"].append({"event_id": event_counter, "key": str(key), "type": "duration", "duration": duration})
        current_pressed[key]["is_released"] = True
        current_pressed[key]["release_time"] = release_time

def log_mouse_movement():
    global last_t, last_x, last_y, event_counter
    # Initialize the time and position variables
    last_t = time.perf_counter()

    # Get the initial position of the mouse
    last_x, last_y = pyautogui.position()

    # Log the mouse position every 0.2 seconds
    while True:
        if stop_listener:
            break
        time.sleep(0.2)
        t = time.perf_counter()
        x, y = pyautogui.position()
        dt = t - last_t
        last_t = t

        # Calculate the distance moved since the last movement
        dx = x - last_x
        dy = y - last_y
        last_x = x
        last_y = y

        # Calculate the velocity and acceleration
        velocity = (dx**2 + dy**2)**0.5 / dt
        acceleration = velocity / dt

        # Increment event counter and add event to data
        event_counter += 1
        data["data"].append({"event_id": event_counter, "x": x, "y": y, "velocity": velocity, "acceleration": acceleration, "type": "move"})

def main():
    global last_x, last_y, last_t

    filename = generate_filename()

    with MouseListener(on_click=on_click) as mouse_listener:
        with KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
            log_mouse_movement()

    with open(folder_path + filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    main()