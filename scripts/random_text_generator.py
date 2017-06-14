#Script responsavel por criar os dados

import collections
import os

seed = "1092384956781341341234656953214543219"
words = open("/home/marcella/PycharmProjects/compactador_de_arquivos/data/lorem_base_text.txt", "r").read().replace("\n", '').split()

def fdata():
    a = collections.deque(words)
    b = collections.deque(seed)
    while True:
        yield ' '.join(list(a)[0:1024])
        a.rotate(int(b[0]))
        b.rotate(1)

g = fdata()
size = 2048000000 #512mb
fname = "/home/marcella/PycharmProjects/compactador_de_arquivos/data/2048mb_file"
fh = open(fname, 'w')
while os.path.getsize(fname) < size:
    fh.write(g.next())
