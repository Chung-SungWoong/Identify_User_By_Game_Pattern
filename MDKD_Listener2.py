# Import the pynput library and time module
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import pyautogui
import time

# Define the functions for the mouse and keyboard listeners
"""
우선 on_move 를 없에고 안의 내용을 밑의 while: 아래에 넣어야 할 것 같음
"""

def on_move(x, y):
    global last_x, last_y, last_t
    # Calculate the time since the last movement
    t = time.perf_counter()
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
    
    print('{0},velocity {1:.2f}, acceleration {2:.2f}'.format((x, y), velocity, acceleration))

def on_click(x, y, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

def on_press(key):
    print('{0} pressed'.format(key))

def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop the listener
        return False

# Set up the mouse and keyboard listeners
with MouseListener(on_move=on_move, on_click=on_click) as mouse_listener:
    with KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
        # Initialize the time and position variables
        last_t = time.perf_counter()
        
        # Get the initial position of the mouse
        last_x, last_y = pyautogui.position()
        
        # Log the mouse position every 0.2 seconds
        while True:
            time.sleep(0.2)
            print(last_x,last_y)