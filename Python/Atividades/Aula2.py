# -*- coding: utf-8 -*-
import math

'''f = 8.5
r = round(f) #arredondar
print(r)
r = math.ceil(f) #arredonda pra mais
print(r)
r = math.floor(f) #arredonda pra menos
print(r)

First=(input('Digite o primeiro valor: '))
Second=int(input('Digite o Segundo valor: '))
print(type(First)) #mostra o tipo do dado
print(type(Second))

#exercicio 1
A = int(input())
B = int(input())
X = A+B
print("X =",X)

#exercicio 2
n = 3.14159
raio = float(input())
area = (n * raio**2)
print("A=%.4f"%area)

#exercicio 3
codFunc = int(input())
hTrab = int(input())
vHora = float(input())
salario = hTrab * vHora
print("Número = ",codFunc,"\nSalário = R$ %.2f"%salario)

#exercicio 4
Dist = int(input())
tComb = float(input())
gastos = Dist / tComb
print("%.3f"%gastos + " km/l")

#exercicio 5
idade = int(input())
anos = int(idade/365)
sobra = idade - anos * 365
meses = int(sobra / 30)
dias = sobra - meses * 30

print(anos,"ano(s)")
print(meses,"mes(es)")
print(dias,"dia(s)")

ln1 = input().split(" ")
ln2 = input().split(" ")

distancia = math.sqrt((float(ln2[0])-float(ln1[0]))**2
                      +(float(ln2[1])-float(ln1[1]))**2)
print("%.4f"%distancia)

A = int(input())
B = int(input())
C = int(input())
D = int(input())

dif = (A * B - C * D)

print("DIFERENCA = ",dif)'''

Y = int(input())
Dist = Y * 2

print(Dist,"minutos")

A = float(input())
B = float(input())
C = float(input())

Med = (A*2+B*3+C*5)/10

print("MEDIA = %.1f"%Med)
