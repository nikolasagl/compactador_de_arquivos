#!-*- coding: utf8 -*-

#MODULO PARA O TAR.GZ

import get_file_csv
import csv

dictcodigo = {
    'codigo1':'tar',
    'codigo2':'-cvzf',
    'nome_arq':'targz.tar.gz'
}

dictarquivo = {
    1:'/home/marcella/PycharmProjects/compactador_de_arquivos/data/8mb_file',
}

compacted_file_size = ''

with open('/home/marcella/PycharmProjects/compactador_de_arquivos/csv/targz/targz.csv', 'wb') as csvfile:
    header = ['User-Time', 'System-Time', 'Elapsed-Time', 'CPU-Usage', 'Compacted-File-Size']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
csvfile.close()

for i in range(50):
    compacted_file_size = get_file_csv.csv_creator(dictcodigo['codigo1'], dictcodigo['codigo2'], dictcodigo['nome_arq'], dictarquivo[1], compacted_file_size, i, True)