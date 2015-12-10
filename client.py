#!/usr/bin/python
from socket import *


#Mensagem 1
# def server_files_list_request():
#     cmd = "get_file_list"
#     message = ("cmd", cmd)
#     return message


# #Mensagem 3
# def server_file_request(file_name):
#     cmd = "get_file"
#     message = [[], "cmd", cmd, "file_name", file_name]
#     return message


s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 50000))

while 1:
    print "Ouvindo conexao"
    data, addr = s.recvfrom(5000)
    print "Recebido %s" % data