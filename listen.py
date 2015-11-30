#!/usr/bin/python
from time import *
from socket import *
import socket
import time
import threading 	#Alterado este import
import Util 		#Inserido este import

def server_listen(TCP_PORT, TCP_IP):

	BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Antes Bind")
	s.bind(('', TCP_PORT))
	s.listen(1)
	#print(s)
	conn, addr = s.accept()
	print 'Connection address:', addr
	while 1:
	    data = conn.recv(BUFFER_SIZE)
	    if not data: break
	    print "received data:", data
	    conn.send(data)  # echo
	conn.close()


TCP_IP = '10.0.0.101'
TCP_PORT = 60000
BUFFER_SIZE = 1024
server_listen(TCP_PORT, TCP_IP)