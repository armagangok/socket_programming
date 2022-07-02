import socket

HEADER = 64
PORT = 5050
FORMAT =  "utf-8"
DISCONNECT_MESSAGE =  "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())  # to get ip address programmatically
ADRESS = (SERVER,PORT)