import pynput
from pynput import mouse

import sys
import time
SECS = 480
global start
global start_location
global start_switch
global prev_x
global m_end
global count
global drag

def on_move(x, y):
    global prev_x
    global m_end
    global count
    global start_switch
    global start_location

    if start_switch == 0:
        start_location = (x, y)
        start_switch += 1
        prev_x = start_location[0]
        m_end = time.time() - 1e-2
    speed = (abs(prev_x - x))/(time.time() - m_end)
    acc = (time.time() - m_end)/(speed + 1e-5)
    print(time.time(), ';', x, ';', y, ';', -1, ';', -1, ';', start_location[0] - x, ';', start_location[1] - y, ';', speed, ';', acc, ';')
    prev_x = x
    m_end = time.time()
    listener.stop()


def on_click(x, y, button, pressed):
    global start
    global drag
    if str(button) == "Button.left":
        button = 0
    elif str(button) == "Button.right":
        button = 2
    else:
        button = 1
    end = time.time()
    formatted_time = "{:.5f}".format(end - start)
    if pressed:
        drag = time.time()
        print(time.time(), ';', x, ';', y, ';', button, ';', formatted_time, ';', start_location[0] - x, ';',
              start_location[1] - y, ';', -1, ';')
    if not pressed:
        if button == 0:
            release = 5
        elif button == 2:
            release = 6
        else:
            release = 7
        try:
            formatted_time = "{:.5f}".format(time.time() - drag)
            print(time.time(), ';', x, ';', y, ';', release, ';', formatted_time, ';', start_location[0] - x, ';',
                  start_location[1] - y, ';', -1, ';')
        except NameError:
            click = time.time()
            print(time.time(), ';', x, ';', y, ';', button, ';', formatted_time, ';', start_location[0] - x, ';',
                  start_location[1] - y, ';', -1, ';')
            formatted_time = "{:.5f}".format(time.time() - click)
            print(time.time(), ';', x, ';', y, ';', release, ';', formatted_time, ';', start_location[0] - x, ';',
                  start_location[1] - y, ';', -1, ';')
    start = time.time()
    listener.stop()


if __name__ == '__main__':
    count = 0
    start_switch = 0
    start = time.time()
    now = time.time()
    end = now + SECS
    flag = True
    while time.time() < end:
        with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
            listener.join()
    listener.stop()