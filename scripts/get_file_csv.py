#!-*- coding: utf8 -*-
import subprocess
import re
import csv

def compact_file(nome_arq):
    size_command = ['du', '-hsb', nome_arq]
    size = subprocess.Popen(size_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    result_size = size.stdout
    size = result_size.readlines()
    compacted_file_size = (re.sub(r'[^\d]+', '', size[0]))
    return compacted_file_size

def csv_creator(codigo1, codigo2, nome_arq, arquivo, compacted_file_size, index, is_tar):
    time_command = ['time', codigo1, codigo2, nome_arq, arquivo]
    time = subprocess.Popen(time_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    result_time = time.stderr
    time = result_time.readlines()

    if is_tar:
        time.pop(0)

    output = []
    for item in [time[0]]:
        items = item.split(' ')
        output.append(items)

    user, system, elapsed, cpu = output[0][0], output[0][1], output[0][2], output[0][3]
    user = (re.sub(r'[^\d.]+','', user))
    system = (re.sub(r'[^\d.]+','', system))
    elapsed = (re.sub(r'[^\d.:]+','', elapsed))
    cpu = (re.sub(r'[^\d.%]+','', cpu))
    if (index == 0):
        compacted_file_size = compact_file(nome_arq)

    print user
    print system
    print elapsed
    print cpu
    print compacted_file_size
    print ''

    aux = [user, system, elapsed, cpu, compacted_file_size]
    with open('/home/marcella/PycharmProjects/compactador_de_arquivos/csv/targz/targz.csv', 'ab') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(aux)
    csvfile.close()
    return compacted_file_size