#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import *
from socket import *
import socket
import time
import thread
import Util

def send_files_list(TCP_IP, PORT_IP):
	cmd = "get_file_list"
	message = [[], ("cmd", cmd)]
	files = ""

	for item in Util.get_files_in_directory(Util.local_files_path):
		files += item + ";"

	message.append(("files", files))

	print(message)

	# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# s.connect((TCP_IP, PORT_IP))
	# s.send(MESSAGE)
	# data = s.recv(BUFFER_SIZE)
	# s.close()

send_files_list('', 60000)