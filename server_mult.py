#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import *
from socket import *
import socket
import time
import threading 	#Alterado este import
import Util 		#Inserido este import
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
		print "%s-%s-%s %s:%s:%s\tEnviando broadcast... " % localtime()[:6]
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

#Servidor Mensagem
def server_listen(TCP_PORT, TCP_IP):

	BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Antes Bind")
	s.bind(('', TCP_PORT))
	s.listen(1)
	print(s)
	conn, addr = s.accept()
	print("Sem ConexS")
	print 'Connection address:', addr
	while 1:
	    data = conn.recv(BUFFER_SIZE)
	    if not data: break
	    print "received data:", data
	    conn.send(data)  # echo
	conn.close()

#Observação utlizado método de Threading https://docs.python.org/2/library/threading.html#thread-objects
# https://docs.python.org/2/library/threading.html

try :
	t = threading.Thread(name='listen', target=server_listen, args=  (300, '10.0.0.100'))
	t.start()
	t.join()

	#thread.start_new_thread(server_listen, (60000, '10.0.0.101'))
except:
	print "Erro: não foi possível criar uma thread"
	# while True:
	# 	t.join()
	# 	#send_files_list('10.0.0.102', 60000)
	# 	pass