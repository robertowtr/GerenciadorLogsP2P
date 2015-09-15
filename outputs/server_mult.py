#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import *
from socket import *
import thread

def listen():
	sclient = socket(AF_INET, SOCK_DGRAM)
	sclient.bind(('', 50000))
	while True:
		print("Ouvindo conexao")
		data, addr = sclient.recvfrom(64)
		print "Recebido %s %s " % (data, addr)

def server():
	server = socket(AF_INET, SOCK_DGRAM)
	server.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
	cont = 0
	while True:
		print "%s-%s-%s %s:%s:%s\tEnviando broadcast..." % localtime()[:6]
		cont += 1
		data = repr(time()) + " cont: " + str(cont) + '\n'
		server.sendto(data, ('<broadcast>', 50000))
		sleep(1)

try:
	thread.start_new_thread(server, ())
	thread.start_new_thread(listen, ())
except:
	print "Erro: não foi possível criar uma thread"

while True:
	pass