
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

def on_press(key):
    print("Key pressed: {0}".format(key))

def on_release(key):
    print("Key released: {0}".format(key))

def on_move(x, y):
    print("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
    else:
        print('Mouse released at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))


keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
mouse_listener = MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()
