#!/usr/bin/python
from time import *
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
	print "%s-%s-%s %s:%s:%s\tEnviando broadcast..." % localtime()[:6]
	data = repr(time()) + '\n'
	s.sendto(data, ('<broadcast>', 50000))
	sleep(1)
