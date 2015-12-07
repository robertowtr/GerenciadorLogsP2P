#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import *
from socket import *
import socket
import time
import threading 	#Alterado este import
import Util 		#Inserido este import
import binascii		#Encode para Texto

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

	print("Request")
	global data_teste
	msg = data_teste

	received_files = msg.split(",")
	received_files = received_files[-1].split(';')

	local_files = ""
	str_final = ""

	for item in Util.get_files_in_directory(Util.local_files_path):
		local_files += item + ";"

	local_list_files = local_files.split(';')

	needed_files = set(received_files) - set(local_list_files)

	for i in needed_files:
	    str_final += i + ';'
	print str_final
	#return str_final

	#Envio
	# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# s.connect((TCP_IP, PORT_IP))
	# s.send(str_final)
	# data = s.recv(BUFFER_SIZE)
	# s.close()

	global state
	state = "final"
	#return message

#Mensagem 2
def send_files_list(TCP_IP, PORT_IP):
	cmd = "get_file_list"
	message = [[], ("cmd", cmd)]
	files = ""

	for item in Util.get_files_in_directory(Util.local_files_path):
		files += item + ";"

	message.append(("files", files))

	MESSAGE = str(message)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, PORT_IP))
	s.send(MESSAGE)
	#data = s.recv(BUFFER_SIZE)
	s.close()

	global state
	state = "final"

#Servidor Mensagem
def server_listen(TCP_PORT, TCP_IP):
	global data_teste
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
	    data_teste = data
	    conn.send(data)  # echo
	conn.close()
	global state
	state = "get_file_list"


def get_ip():
	print "inicial"
	return socket.gethostbyname(socket.gethostname())
#Observação utlizado método de Threading https://docs.python.org/2/library/threading.html#thread-objects
# https://docs.python.org/2/library/threading.html

def input_file(nome_arq):
  with open(nome_arq, "rb") as f:
    byte = f.read()
  return byte

def output_file(out_info, out_name):
  arq_out = open(out_name, "wb+")
  arq_out.write(out_info)
  arq_out.close()

def encode_file(nome_arq):
	datainput = binascii.rlecode_hqx(input_file(nome_arq))
	return datainput

def decode_file(nome_arq):
	dataoutput = binascii.rledecode_hqx(output_file(nome_arq))
	return dataoutput



try :
	iplocal = str(get_ip())
	print "Ouvindo broadcast"

	t = threading.Thread(name='ouvindoinicio', target= listen)
	t.start()
	t.join()

	state = "inicial"		#Variável state indica qual estado se encontra o programa
	while  1:
		print state
		if state == "inicial":
			t = threading.Thread(name='listen', target=server_listen, args=  (60000, iplocal))
			t.start()
			t.join()
			print "Loop"
		if state == "sendlist":
			t = threading.Thread(name='sendlist', target=send_files_list, args=  (60000, '10.0.0.101'))
			t.start()
			t.join()
			print("Lista")

		if state == "get_file_list":
			t = threading.Thread(name='get_file_list', target=server_files_list_request, args=  (60000, '10.0.0.101'))
			t.start()
			t.join()

		if state == "final":
			break


	#t.join() #Esta função faz que se aguarde o fim da Thread a omitindo ela executa automáticamente
	print "FIM"


	#thread.start_new_thread(server_listen, (60000, '10.0.0.101'))
except:
	print "Erro: não foi possível criar uma thread"
	# while True:
	# 	t.join()
	# 	#send_files_list('10.0.0.102', 60000)
	# 	pass