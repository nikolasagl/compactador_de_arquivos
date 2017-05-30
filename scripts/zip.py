#!-*- coding: utf8 -*-

#MODULO PARA O ZIP

################################################## OBSERVAÇÃO #######################################################
#para que o modulo do ZIP funcione é preciso trocar o valor da variavel erro passado a listaux no modulo 'get_time'
#trocar para: listaux = erro[0]

import get_file_csv
import csv

dictcodigo = {
    'codigo1':'zip',
    'codigo2':'-r',
    'nome_arq':'zip.zip'
}

dictarquivo = {
    1:'/home/marcella/PycharmProjects/compactador_de_arquivos/data/8mb_file',
}

#cria um arquivo csv e define seu cabeçalho
with open('/home/marcella/PycharmProjects/compactador_de_arquivos/csv/zip/zip.csv', 'wb') as csvfile:
    header = ['User-Time', 'System-Time', 'Elapsed-Time', 'CPU-Usage','Compacted-File-Size']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
csvfile.close()

#laço que chama a função responsavel por captar os dados de cada compactação e escreve-los em uma nova linha o arquivo csv
teste = get_file_csv.csv_creator(dictcodigo['codigo1'], dictcodigo['codigo2'], dictcodigo['nome_arq'], dictarquivo[1], '', 0, False, False, True)

print teste