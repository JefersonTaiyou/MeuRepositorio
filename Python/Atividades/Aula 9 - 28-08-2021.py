# -*- coding: utf-8 -*-
'''
Continuação da aula 8 sobre funções
'''

def calcula(n, n3, n2):
    return n2 - n * n3 % n

n=3
n2=5
n3=7

print(calcula(n3,n2,n))

def soma(a,b):
    return  a+b
def subt(a,b):
    return a-b

n=soma(4,3)
n2=subt(10,2)
n3=n+n2

print(n3)


def addList(list,elem):
    list.append(elem)

lista = [10]
addList(lista,20)
addList(lista,0)

print(lista)

def addLista(list,elem):
    list.append(elem)
    return list

lista = [20,30]
lista2 = lista

addLista(lista2,40)

lista2[0]=-1
lista2[1]=-2
lista2[2]=-3

print(lista)