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

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

with MouseListener(on_click=on_click, on_move=on_move) as listener:
    with KeyboardListener(on_press=on_press) as listener:
        listener.join()
        time.sleep(0.2)


"""
from pynput.mouse import Controller as mouse_control
from pynput import keyboard as key_control

mouse = mouse_control() #mouse controller

def on_press (key) :
    print(key.char)

listener = key_control.Listener(on_press=on_press) #keyboard listener
listener.start()

while True :
    command = mouse.position
    print(command)
    time.sleep(0.2)

"""