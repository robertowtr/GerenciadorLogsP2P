#!/usr/bin/python
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 50000))

while 1:
	print "Ouvindo conexao"
	data, addr = s.recvfrom(64)
	print "Recebido %s" % data
