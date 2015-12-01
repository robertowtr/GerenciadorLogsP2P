#!/usr/bin/python
import binascii


def input_file(nome_arq):
  with open(nome_arq, "rb") as f:
    byte = f.read()
  return byte

def output_file(out_info, out_name):
  nome_cypt = str(out_name[0:-3]) + "dec"
  arq_out = open(nome_cypt, "wb+")
  arq_out.write(out_info)
  arq_out.close()


datainput = binascii.rlecode_hqx(input_file('FF.txt'))

#print(datainput)

output_file( datainput, 'FF.txt')

dataoutput = binascii.rledecode_hqx(datainput)

output_file(dataoutput, "FFO.txt")

#print(dataoutput)