#!/usr/bin/env python

import socket


TCP_IP = '10.0.0.102'
TCP_PORT = 300
BUFFER_SIZE = 1024
MESSAGE = "Mensagaem De Texto"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
#data = s.recv(BUFFER_SIZE)
s.close()
print "Enviado"
#print "received data:", data