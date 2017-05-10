#!-*- coding: utf8 -*-

#MODULO PARA O RAR

################################################## OBSERVAÇÃO #######################################################
#para que o modulo do RAR funcione é preciso trocar o valor da variavel erro passado a listaux no modulo 'get_time'
#trocar para: listaux = erro[0]

import get_time
import csv

dictcodigo = {
    'codigo1':'rar',
    'codigo2':'a',
    'nome_arq':'rar.tar'
}

dictarquivo = {
    1:'/home/nikolas/BIOQUÍMICA/arquivo1',
    2:'/home/nikolas/BIOQUÍMICA/arquivo2',
    3:'/home/nikolas/BIOQUÍMICA/arquivo3',
    4:'/home/nikolas/BIOQUÍMICA/arquivo4',
    5:'/home/nikolas/BIOQUÍMICA/arquivo5'
}

#cria um arquivo csv e define seu cabeçalho
with open('/home/marcella/PycharmProjects/compactador_de_arquivos/csv/rar/rar.csv', 'wb') as csvfile:
    header = ['User-Time', 'System-Time', 'Elapsed-Time', 'CPU-Usage']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()

#laço que chama a função responsavel por captar os dados de cada compactação e escreve-los em uma nova linha o arquivo csv
for i in range(len(dictarquivo)):
    teste = get_time.csv_creator(dictcodigo['codigo1'], dictcodigo['codigo2'], dictcodigo['nome_arq'], dictarquivo[i+1])

csvfile.close()
print teste