#!-*- coding: utf8 -*-

#MODULO PARA O ZIP

import get_file_csv
import csv
import sys

dictcodigo = {
    'codigo1':'zip',
    'codigo2':'-r',
    'nome_arq':'zip.zip'
}

dictarquivo = {
    1: str(sys.argv[1]),
}

compacted_file_size = ''

with open(str(sys.argv[2]), 'wb') as csvfile:
    header = ['User-Time', 'System-Time', 'Elapsed-Time', 'CPU-Usage','Compacted-File-Size']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
csvfile.close()

for i in range(200):
    compacted_file_size = get_file_csv.csv_creator(dictcodigo['codigo1'], dictcodigo['codigo2'], dictcodigo['nome_arq'], dictarquivo[1], compacted_file_size, i, False, str(sys.argv[2]))
