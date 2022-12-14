# Import the pynput library and time module
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime
import pyautogui
import time
import logging
global last_x, last_y, last_t

# Define the functions for the mouse and keyboard listeners

logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def end_rec(key):
    logging.info(str(key))

def on_click(x, y,button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_press(key):
    print('{0} pressed'.format(key))
    current_pressed.add(key)
    logging.info("key %s pressed: " %key)

current_pressed = set()

def on_release(key):
    print('{0} release'.format(key))
    logging.info("key %s released: " %key)

    if key in current_pressed:
        current_pressed.remove(key)  
    

# Set up the mouse and keyboard listeners
with MouseListener(on_click=on_click) as mouse_listener:
    with KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
        # Initialize the time and position variables
        last_t = time.perf_counter()
        
        # Get the initial position of the mouse
        last_x, last_y = pyautogui.position()

        # Log the mouse position every 0.5 seconds
        while True:
            time.sleep(0.5)
            s = datetime.fromtimestamp(time.time())
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
            logging.info("Mouse moved to ({0}, {1})".format(x, y))
            print('{0},velocity {1:.2f}, acceleration {2:.2f}, Date:{3}'.format((x, y), velocity, acceleration, s))
