#!/usr/bin/python
from time import *
from socket import *
import socket
import time
import threading 	#Alterado este import
import Util 		#Inserido este import
import binascii		#Encode para Texto


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

def decode_file(data_input, nome_arq):
	dataoutput = binascii.rledecode_hqx(output_file(data_input, nome_arq))
 	return str(dataoutput)

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
    		print "received data:",  data
    		conn.send(data)  # echo
	conn.close()
	return str(data)


TCP_IP = '10.0.0.103'
TCP_PORT = 60000
BUFFER_SIZE = 1024
tx = server_listen(TCP_PORT, TCP_IP)
decode_file(tx, "teste.txt")