from operator import imod
import socket
import threading
from src.constants.constants import *





# AF_INET -> socket type
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

adress = (SERVER, PORT)

socket.bind(ADRESS)

# to get ip address in terminal run that command -> $ ipconfig getifaddr en0




  

def handleClient(connection, adress):
  print(f"[NEW CONNECTION] {adress} connected.")
  
  isConnected = True;
  
  while isConnected:
    messageLength = connection.recv(HEADER).decode(FORMAT)
    if messageLength:
      messageLength = int(messageLength)
      message = connection.recv(HEADER).decode(FORMAT)
      if message == DISCONNECT_MESSAGE:
        isConnected = False
      print(f"[{adress}] {message}")
      connection.send("Message received properly.".encode(FORMAT))
      
      
  connection.close()    


##
##

    
def start():
  socket.listen()
  print(f"[LISTENING] Server is listening on {SERVER}")
  
  while True:
    connection, adress = socket.accept()
    thread = threading.Thread(target=handleClient,args=(connection,adress))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    
  
  
  