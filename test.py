#!/usr/bin/python
from time import *
from socket import *
import socket
import time
import threading 	#Alterado este import
import Util 		#Inserido este import

cmd = "get_file_list"
message = [[], ("cmd", cmd)]
files = ""

for item in Util.get_files_in_directory(Util.local_files_path):
	files += item + ";"

message.append(("files", files))
print message