import Util
from time import *


lista_logs = []
lista_logs_terceiros = []

path_logs = "./outputs/"
path_logs_terceiros = "./inputs/"


def start():
    while(True):
        #check_incoming_connections()
        criar_arquivo_log()


#Criacao dos arquivos de logs local
def criar_arquivo_log():
    output_file = ""
    file_name = ""
    #Geracao do conteudo e apenas um for que ira inserir os numericos
    for i in range(0, 1000):
        sleep(1)
        output_file += str(i)

    #Gravacao do arquivo de log no diretorio padrao 'outputs'
    file_name = "./outputs/" + str(Util.get_local_ip()) + "." + str(Util.get_time()) + ".txt"
    Util.write_file(file_name, output_file)
    lista_logs.append(file_name)

def atualizar_lista_logs():
    lista_logs = Util.get_files_in_directory(path_logs)
    lista_logs_terceiros = Util.get_files_in_directory(path_logs_terceiros)

atualizar_lista_logs()