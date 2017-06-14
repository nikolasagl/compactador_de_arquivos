#!-*- coding: utf8 -*-

#MODULO PARA O TAR.GZ

import get_file_csv
import csv
import sys

dictcodigo = {
    'codigo1':'tar',
    'codigo2':'-cvzf',
    'nome_arq':'targz.tar.gz'
}

dictarquivo = {
    1: str(sys.argv[1]),
}

compacted_file_size = ''

with open(str(sys.argv[2]), 'wb') as csvfile:
    header = ['User-Time', 'System-Time', 'Elapsed-Time', 'CPU-Usage', 'Compacted-File-Size']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
csvfile.close()

for i in range(200):
    compacted_file_size = get_file_csv.csv_creator(dictcodigo['codigo1'], dictcodigo['codigo2'], dictcodigo['nome_arq'], dictarquivo[1], compacted_file_size, i, True, str(sys.argv[2]))
