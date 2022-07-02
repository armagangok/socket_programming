import socket
from constants.constants import *


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADRESS)


def sendMessage(message):
  message = message.encode(FORMAT)
  messageLength = len(message)
  sendLength = str(messageLength).encode(FORMAT)
  sendLength += b' ' * (HEADER -len(sendLength))
  client.send(sendLength)
  client.send(message)
  print(client.recv(2048).decode(FORMAT))
  

sendMessage("hi there! This message is sending by Armağan.")
sendMessage(DISCONNECT_MESSAGE)
