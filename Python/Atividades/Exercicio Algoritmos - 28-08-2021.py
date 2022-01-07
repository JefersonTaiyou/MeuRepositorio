# -*- coding: utf-8 -*-

print("9\n7\n5\n3\n1")

for n in range(9,0,-2):
    print(n)

var=0
while var < 11:
    var +=1
    if (var%3==0):
        print(var)

n=10//5

print(n)

n = 5 - 10
c1 = -10 > n
c2 = -15 > n
r1 = c1 or c2
r2 = c1 and c2
print(c1, c2)
print(r1, r2)

n = 10 % 2
c1 = 9 > n
c2 = 0 > n
r1 = not c1 and c2
r2 = c1 or not c2
print(c1, c2)
print(r1, r2)

n = 2 + 3 * 5
r1 = not not True
r2 = not (10 < n or n == 17)
c1 = 20 < n or 20 > n and n > 10
c2 = n > 0 or 12 <= n and 'monty python'
print(n, r1, r2)
print(c1, c2)

a = int(input())
b = int(input())
if (a > b):
    print("Maior")
if (a == b):
    print("Igual")
else:
    print("Menor")

lista = [0, 1, "João", "Maria"]
tamanho = len(lista)
for i in range(tamanho):
    print(lista[i])

cont = 10
for c in range(cont):

    file = 'screenShot{:03d}.jpg'.format(c)

    print(file)

lista = ["Mario", "Maroi", "Mario", "Maria"]
for a in lista:
    if (a == "Mario"):
        for n in range(50,60+1):
                print(n)
print("Fim")

n = int(input())
lista = []
for i in range(n) :
    lista.append(input())

for i in range(len(lista)) :
    if len(lista[i])>=9:
        print(lista[i])


'''

1
- Sim
- Não
- Sim
- Não
- Sim
- Sim
- Não
- Sim
- Sim
- Sim

2
- -5
- True
- 2, True
- not c = False
- False False / False False
- True False / False True
- 17 True False / True True

3
- 12.5
- 10
- 10
- Menor

a = int(input())
b = int(input())
if (a > b):
    print("Maior")
if (a == b):
    print("Igual")
else:
    print("Menor")

4
- Um Loop infinito de 10
- print("9\n7\n5\n3\n1")
- for n in range(9,0,-2):
    print(n)
- var=0
while var < 11:
    var +=1
    if (var%3==0):
        print(var)


5
- 0 / 1 / João / Maria
- 3 4 3 4
- lista = ["Mário", "Mároi", "Mário", "Maria"]
for a in lista:
    if (a == "Mário"):
        for n in range(50,60+1):
                print(n)
print("Fim")
- lista = ["Mário", "Mároi", "Mário", "Maria"]
for a in lista:
    if (a == "Mário"):
        for n in range(50,60+1,2):
                print(n)
print("Fim")
- n = int(input())
lista = []
for i in range(n) :
    lista.append(input())

for i in range(len(lista)) :
    if len(lista[i])>=9:
        print(lista[i])

Gatu
Biel
Keviney
Keven
Rodrigo
Japa

Deel
Gardem
Chaguinha
Elayne
Gean
Carla
Leo
Viny
Vitoria
Sabrina
Fran
Marcelo
Chaxá
Gabriel
Ruiva

Gui <3
Guilherme

Thauanny
Livia

Gustavo

Luciano
Giovane
Daniel
Giovana

'''