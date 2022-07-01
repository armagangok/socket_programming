import socket
import threading


PORT = 5050


# to get ip address in terminal run that command -> $ ipconfig getifaddr en0
# SERVER  = "192.168.1.36"



# to get ip address programmatically
def getIp():
  SERVER = socket.gethostbyname(socket.gethostname())
  return SERVER




