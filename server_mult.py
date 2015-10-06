#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import *
from socket import *
import thread
BUFFER_SIZE = 1024

def listen():
	sclient = socket(AF_INET, SOCK_DGRAM)
	sclient.bind(('', 50000))
	while True:
		print("\nOuvindo conexao")
		data, addr = sclient.recvfrom(64)
		print "Recebido %s %s " % (data, addr)
		print addr[0]

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

def server_files_list_request(TCP_IP, PORT_IP):

	cmd = "get_file_list"
    message = ("cmd", cmd)
    #Envio
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, PORT_IP))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
    #return message

#Mensagem 2
def send_files_list(TCP_IP, PORT_IP):
    cmd = "get_file_list"
    message = [[], ("cmd", cmd)]
    files = ""

    for item in Util.get_files_in_directory(Util.local_files_path):
        files += item + ";"

    message.append(("files", files))
    
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, PORT_IP))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()


try:
	thread.start_new_thread(server, ())
	thread.start_new_thread(listen, ())
except:
	print "Erro: não foi possível criar uma thread"

while True:
	pass