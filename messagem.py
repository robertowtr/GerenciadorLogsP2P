#!/usr/bin/python
from time import *
from socket import *
import socket
import time
import threading 	#Alterado este import
import Util 		#Inserido este import



TCP_IP = '10.0.0.101'
TCP_PORT = 60000
BUFFER_SIZE = 1024
#MESSAGE = "Mensagaem De Texto"

# cmd = "get_file_list"
# message = [[], ("cmd", cmd)]
# files = ""

# for item in Util.get_files_in_directory(Util.local_files_path):
# 	files += item + ";"

# message.append(("files", files))

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


message = encode_file('FF.txt')

MESSAGE = str(message)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
#data = s.recv(BUFFER_SIZE)
s.close()
print "Enviado"
#print "received data:", data