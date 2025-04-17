from pynput import keyboard
import time

def on_press(key, injected):
    try:
        print('alphanumeric key {} pressed; it was {}'.format(
            key.char, 'faked' if injected else 'not faked'))
    except AttributeError:
        print('special key {} pressed'.format(
            key))

def on_release(key, injected):
    print('{} released; it was {}'.format(
        key, 'faked' if injected else 'not faked'))
    current_time = time.ctime()
    print("Current time in seconds since the epoch:", current_time)
    
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()