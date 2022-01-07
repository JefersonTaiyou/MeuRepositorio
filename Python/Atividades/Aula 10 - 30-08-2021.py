# -*- coding: utf-8 -*-
'''
Criar um jogo de Xadrez usando Matrizes
'''

n=2
mat=[]

for i in range(n):
    lista=[]
    for j in range(n):
        lista.append(-1)
    mat.append(lista)
print(mat)

n=2
mat=[]

for i in range(n):
    lista=[]
    for j in range(n):
        if (i%2==0):
            lista.append('X')
        else:
            lista.append('Y')
    mat.append(lista)
print(mat)

n=3
mat=[]

for i in range(n):
    lista=[]
    for j in range(n):
        if ((i+j)%2==0):
            lista.append('X')
        else:
            lista.append('Y')
    mat.append(lista)
print(mat)