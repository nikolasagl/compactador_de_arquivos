#!-*- coding: utf8 -*-

#MODULO PARA O TAR.GZ

################################################## OBSERVAÇÃO #######################################################
#para que o modulo do TAR.GZ funcione é preciso trocar o valor da variavel erro passado a listaux no modulo 'get_time'
#trocar para: listaux = erro[1]

import get_file_csv
import csv

dictcodigo = {
    'codigo1':'tar',
    'codigo2':'-cvzf',
    'nome_arq':'targz.tar.gz'
}

dictarquivo = {
    1:'/home/marcella/PycharmProjects/compactador_de_arquivos/data/file',
    2:'/home/marcella/PycharmProjects/compactador_de_arquivos/data/file',
    3:'/home/marcella/PycharmProjects/compactador_de_arquivos/data/file',
    4:'/home/marcella/PycharmProjects/compactador_de_arquivos/data/file',
    5:'/home/marcella/PycharmProjects/compactador_de_arquivos/data/file'
}

#cria um arquivo csv e define seu cabeçalho
with open('/home/marcella/PycharmProjects/compactador_de_arquivos/csv/targz/targz.csv', 'wb') as csvfile:
    header = ['User-Time', 'System-Time', 'Elapsed-Time', 'CPU-Usage']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()

#laço que chama a função responsavel por captar os dados de cada compactação e escreve-los em uma nova linha o arquivo csv
for i in range(len(dictarquivo)):
    teste = get_file_csv.csv_creator(dictcodigo['codigo1'], dictcodigo['codigo2'], dictcodigo['nome_arq'], dictarquivo[i + 1])

csvfile.close()
print teste