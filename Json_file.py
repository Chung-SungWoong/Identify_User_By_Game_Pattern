from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput import keyboard
from datetime import datetime
import pyautogui
import cv2
import numpy as np
import time
import json
global last_x, last_y, last_t, stop_listener

stop_listener = False
# Define the functions for the mouse and keyboard listeners

# Initialize data dictionary
data = {"events": []}

# Define a counter for events
event_counter = 0

def end_rec(key):
    global event_counter
    event_counter += 1
    data["events"].append({"event_id": event_counter, "key": str(key), "type": "end_rec"})

# Mouse clicked
def on_click(x, y, button, pressed):
    global event_counter
    event_counter += 1
    data["events"].append({"event_id": event_counter, "x": int(x), "y": int(y), "button": str(button), "pressed": pressed, "type": "click"})

# Keyboard pressed
def on_press(key):
    global stop_listener
    global event_counter
    event_counter += 1
    data["events"].append({"event_id": event_counter, "key": str(key), "type": "press"})

    if key == keyboard.Key.esc:
        stop_listener = True

# Save the pressed button on the current_pressed set
current_pressed = set()

# Keyboard released 
def on_release(key):
    global event_counter
    event_counter += 1
    data["events"].append({"event_id": event_counter, "key": str(key), "type": "release"})

    if key in current_pressed:
        current_pressed.remove(key)  

# Set up the mouse and keyboard listeners
with MouseListener(on_click=on_click) as mouse_listener:
    with KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
        # Initialize the time and position variables
        last_t = time.perf_counter()

        # Get the initial position of the mouse
        last_x, last_y = pyautogui.position()

        # Log the mouse position every 0.2 seconds
        while True:
            if stop_listener:
                break
            time.sleep(0.1)
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
            data["events"].append({"event_id": event_counter, "x": x, "y": y, "velocity": velocity, "acceleration": acceleration, "type": "move"})
            
            pyautogui.screenshot(r"C:\Users\dnd88\Desktop\Test\SS".format(time.time()))
            print('saved')
            
            if 'esc' in current_pressed:
                break

with open('/Users/chung_sungwoong/Desktop/Practice/Identify_User_By_Game_Pattern/log.json', 'w') as json_file:
    json.dump(data, json_file)