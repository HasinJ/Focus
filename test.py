# Code to check if left or right mouse buttons were pressed
import time
import pynput.keyboard as keyboard
import pynput.mouse as mouse

#keys
def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == keyboard.Key.esc:
        return False # Stop listener

#clicks
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))


while True:
    # Collect events until released
    with keyboard.Listener(on_release=on_release) as k_listener, mouse.Listener(on_click=on_click) as m_listener:
        #needs to do things before .join()

        k_listener.join()
        m_listener.join()


    time.sleep(0.001)
