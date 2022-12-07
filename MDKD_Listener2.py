
from pynput.keyboard import Listener  as KeyboardListener
from pynput.mouse    import Listener  as MouseListener
from pynput.keyboard import Key
import logging
import time

logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def end_rec(key):
    logging.info(str(key))

def on_press(key):
    logging.info(str(key))

current_pressed = set()

def on_press(key):
    current_pressed.add(key)
    logging.info("key %s pressed: " %key)


def on_release(key):
    logging.info("key %s released: " %key)

    if key in current_pressed:
        current_pressed.remove(key)    

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))



with MouseListener(on_click=on_click) as listener:
    with KeyboardListener(on_press=on_press) as listener:
        listener.join()

"""
from pynput.mouse import Controller as mouse_control
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

from pynput import keyboard as key_control
import time

mouse = mouse_control() #mouse controller

def on_press (key) :
    print(key)

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

with MouseListener(on_click=on_click) as listener:
    with KeyboardListener(on_press=on_press) as listener:
        listener.join()

listener = key_control.Listener(on_press=on_press, on_click = on_click) #keyboard listener
listener.start()
"""