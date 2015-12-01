from time import *
from socket import *
import socket
import time
import threading  #Alterado este import
import Util     #Inserido este import

def get_files_needed(msg):
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
  return str_final