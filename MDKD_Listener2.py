# Import the pynput library and time module
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput import keyboard
from datetime import datetime
import pyautogui
import time
import logging
global last_x, last_y, last_t

# Define the functions for the mouse and keyboard listeners

# Save the data file in the log.txt file
logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def end_rec(key):
    logging.info(str(key))

# Mouse clicked
def on_click(x, y,button, pressed):
    print(f'{int(x)} at {int(y)}'.format('clicked' if pressed else 'Released'))
    if pressed:
        logging.info(f'{int(x)} at {int(y)}'.format('clicked' if pressed else 'Released'))

# Keyboard pressed
def on_press(key):
    print('{0} pressed'.format(key))
    current_pressed.add(key)
    logging.info("key %s pressed: " %key)

    if key == keyboard.Key.esc:
        exit(0)

# Save the pressed button on the current_pressed set
current_pressed = set()


# Keyboard released 
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
            # s = datetime.fromtimestamp(time.time())
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
            logging.info("Velocity:{0:.2f}, Accerleation:{1:.2f}".format(velocity,acceleration))
            # logging.info("Date:{0}".format(s))
            print('saved')
            if 'Key.esc' in current_pressed:
                break


            
