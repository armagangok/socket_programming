from email import message
from multiprocessing import connection
import socket
import threading

HEADER = 64
PORT = 5050
FORMAT =  "utf-8"
DISCONNECT_MESSAGE =  "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())  # to get ip address programmatically
ADDRESS =   (SERVER,PORT)


# AF_INET -> socket type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

adress = (SERVER, PORT)

server.bind(ADDRESS)

# to get ip address in terminal run that command -> $ ipconfig getifaddr en0




  

def handleClient(connection, adress):
  print(f"[NEW CONNECTION] {adress} connected.")
  
  isConnected = True;
  
  while isConnected:
    messageLength = connection.recv(HEADER).decode(FORMAT)
    messageLength = int(messageLength)
    message = connection.recv(HEADER).decode(FORMAT)
    print(f"[{adress}] {message}")
    if message == DISCONNECT_MESSAGE:
      isConnected = False
      
  connection.close()    

##
##
    
def start():
  server.listen()
  print(f"[LISTENING] Server is listening on {SERVER}")
  
  while True:
    connection, adress = server.accept()
    thread = threading.Thread(target=handleClient,args=(connection,adress))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    
  
  
  