from pynput.mouse import Controller as mouse_control
from pynput import keyboard as key_control
import time

mouse = mouse_control() #mouse controller

def on_press (key) :
    print(key.char)

listener = key_control.Listener(on_press=on_press) #keyboard listener
listener.start()

while True :
    command = mouse.position
    print(command)
    time.sleep(0.2)