#!/usr/bin/python
from time import *
from socket import *
import Util


#Mensagem 2
def send_files_list():
    cmd = "get_file_list"
    message = [[], ("cmd", cmd)]
    files = ""

    for item in Util.get_files_in_directory(Util.local_files_path):
        files += item + ";"

    message.append(("files", files))
    return message


#Mensagem 4
def send_file(file_name):
    cmd = "get_file"
    file = Util.scanFile(Util.local_files_path + file_name)
    message = [[], "cmd", cmd, "file_name", file_name, "file", file]
    return message


s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
    print send_files_list()
    print "%s-%s-%s %s:%s:%s\tEnviando broadcast..." % localtime()[:6]
    data = repr(time()) + '\n'
    s.sendto(data, ('<broadcast>', 50000))
    sleep(1)
