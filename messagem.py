#!/usr/bin/python
from time import *
from socket import *
import socket
import time
import threading 	#Alterado este import
import Util 		#Inserido este import


TCP_IP = '10.0.0.102'
TCP_PORT = 60000
BUFFER_SIZE = 1024
#MESSAGE = "Mensagaem De Texto"

cmd = "get_file_list"
message = [[], ("cmd", cmd)]
files = ""

for item in Util.get_files_in_directory(Util.local_files_path):
	files += item + ";"

message.append(("files", files))

MESSAGE = str(message)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
#data = s.recv(BUFFER_SIZE)
s.close()
print "Enviado"
#print "received data:", data