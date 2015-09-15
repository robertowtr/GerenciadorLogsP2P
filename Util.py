import datetime
import socket
from os import listdir
from os.path import isfile, join


#Funcao para fazer a escrita de um arquivo
def write_file(path, message):
    file = open(path, "w")
    file.write(message)
    file.close()


#Funcao de retorno da data e hora atual
def get_time():
    return datetime.datetime.now()


#Funcao de retorno do ip local
def get_local_ip():
    return socket.gethostbyname(socket.gethostname())


#Funcao que retorna lista com o nome dos arquivos em determinado diretorio
def get_files_in_directory(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    return files
