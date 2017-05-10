#!-*- coding: utf8 -*-

#Importando...
import subprocess
import re
import csv

#Definição da função que compacta o arquivo e gera csv com o time de execução da compactação
def csv_creator(codigo1, codigo2, nome_arq, arquivo):
    #comando que será escrito no terminal
    command = ['time', codigo1, codigo2, nome_arq, arquivo]

    #Abre um 'terminal' e executa o comando passado por parametro
    #aqui stderr e stdout recebem um pipe vindo do subprocess popen. obs: nao sei pra que ainda
    p = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    #o time de execução do processo(que é o que queremos) é retornado no stderr
    #stdout retorna a execução do processo em si.(mostra o passo a passo da compactação do arquivo)
    result = p.stderr

    #readlines retorna uma lista de strings, onde cada string representa uma linha de result
    erro = result.readlines()

    #print erro[0]

    #lista que recebera o stderr separado por palavras
    output = []
    #lista aux q recebe apenas a primeira linha de stderr(que é o q interessa, linha q contem, user, sys, elapsed, cpu)
    listaux = [erro[0]]

    #for que separa a linha 1 de stderr por palavras, atraves dos espaços(toda vez q encontra um espaço ' ' ele define uma palavra
    #e joga para dentro da lista output, que passa a ser uma lista de strings, onde cada string representa o valor de uma das variaveis de estudo
    for item in listaux:
        items = item.split(' ')
        output.append(items)

    #cada valor da string output recebe uma variavel correspondente, só pra facilitar a manipulação
    user, system, elapsed, cpu = output[0][0], output[0][1], output[0][2], output[0][3]

    #tratamento das strings. Retira todos caracteres não numericos com exceção dos especificados
    user = (re.sub(r'[^\d.]+','', user))
    system = (re.sub(r'[^\d.]+','', system))
    elapsed = (re.sub(r'[^\d.:]+','', elapsed))
    cpu = (re.sub(r'[^\d.%]+','', cpu))

    #print user
    #print system
    #print elapsed
    #print cpu

    #escreve a variavel aux em uma nova linha no um arquivo csv criado no doc 'targz.py'
    #'ab' do parametro de open refere-se a append b, b vai em todos
    aux = [user, system, elapsed, cpu]
    with open('/home/marcella/PycharmProjects/compactador_de_arquivos/csv/rar/rar.csv', 'ab') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(aux)
        return 0
    return 1
