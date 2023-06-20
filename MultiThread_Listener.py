import threading
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput import keyboard
from datetime import datetime
import pyautogui
import time
import logging

# Only works in Window enviornment
# Set up logging configuration
logging.basicConfig(filename="log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
logging.getLogger("PIL").setLevel(logging.ERROR)

# Mouse clicked
def on_click(x, y, button, pressed):
    if pressed:
        log_msg = f'{int(x)} at {int(y)}'
        logging.info(log_msg)

# Keyboard pressed
def on_press(key):
    logging.info(f"key {key} pressed")

    if key == keyboard.Key.esc:
        exit(0)

# Keyboard released
def on_release(key):
    logging.info(f"key {key} released")

# Log mouse position
def log_mouse_position():
    # Initialize the time and position variables
    last_t = time.perf_counter()

    # Get the initial position of the mouse
    last_x, last_y = pyautogui.position()

    # Log the mouse position every 0.2 seconds
    while True:
        time.sleep(0.1)
        t = time.perf_counter()
        x, y = pyautogui.position()
        dt = t - last_t
        last_t = t

        # Calculate the distance moved since the last movement
        dx = x - last_x
        dy = y - last_y
        if dx != 0 or dy != 0:
            last_x = x
            last_y = y

            # Calculate the velocity and acceleration
            velocity = (dx**2 + dy**2)**0.5 / dt
            acceleration = velocity / dt
            logging.info(f"Mouse moved to ({x}, {y})")
            logging.info(f"Velocity:{velocity:.2f}, Accerleation:{acceleration:.2f}")

        # Save screenshot
        pyautogui.screenshot(f'/Users/chung_sungwoong/Desktop/Practice/Identify_User_By_Game_Pattern/screenshot/SS{time.time():.3f}.png')

# Create mouse and keyboard listener threads
mouse_listener = MouseListener(on_click=on_click)
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
log_mouse_position_thread = threading.Thread(target=log_mouse_position)

# Start the threads
mouse_listener.start()
keyboard_listener.start()
log_mouse_position_thread.start()

# Join the threads
mouse_listener.join()
keyboard_listener.join()
log_mouse_position_thread.join()