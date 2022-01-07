# -*- coding: utf-8 -*-

def main_menu():
    rodar = True
    while True:
        print()
        print(">> Escolha uma das opções:\n"
              "1 - Média Ponderada / 2 - Divisores / 3 - Impar-Par / 4 - Cédulas / 5 - Soma Impares\n"
              "6 - Intervalo / 7 - Ordenação Simples / 8 - Tipo Triangulo / 9 - Triângulo / 10 - Tempo de Jogo\n")
        opc = int(input("Opção: "))

        if opc==1:
            rodar=False
            media_pond()
        elif opc==2:
            rodar=False
            divisor()
        elif opc==3:
            rodar=False
            imp_par_pos_neg()
        elif opc==4:
            rodar=False
            cedulas()
        elif opc==5:
            rodar=False
            sum_impar()
        elif opc==6:
            rodar=False
            intervalo()
        elif opc==7:
            rodar=False
            order_simples()
        elif opc==8:
            rodar=False
            type_trinangulo()
        elif opc==9:
            rodar=False
            triangulo()
        elif opc==10:
            rodar=False
            tempo_jogo()
        else:
            rodar=True
            print(">> Opção inválida, tente novamente")

#Exercicio A - Média Ponderada
def media_pond():
    print(">>>>> Exercicio A - Média Ponderada")
    A = float(input(">> Digite a primeira nota: "))
    B = float(input(">> Digite a segunda nota: "))

    Media = ((A*3.5)+(B*7.5))/11
    print(">> MEDIA {:.5f}".format(Media))

#Exercicio B - Divisor
def divisor():
    print(">>>>> Exercicio B - Divisores")
    aux = 1
    num = int(input(">> Digite um valor para saber seus dividores: "))
    while aux <= num:
        x = num % aux
        aux = aux +1
        if x == 0:
            print (aux-1)

#Exercicio C - Impar/Par/Positivo/Negativo
def imp_par_pos_neg():
    Valores = []
    impar=0
    par=0
    posit=0
    negat=0

    print(">>>>> Exercicio C - Impar/Par/Positivo/Negativo")
    while len(Valores)<5:
        var = int(input("Digite um valor: "))
        Valores.append(var)

        if var < 0:
            negat += 1
        elif var > 0:
            posit += 1

        resto = var % 2
        if resto == 0:
            par += 1
        else:
            impar += 1

    print("{} valor(es) par(es)".format(par))
    print("{} valor(es) impar(es)".format(impar))
    print("{} valor(es) positivo(s)".format(posit))
    print("{} valor(es) negativo(s)".format(negat))

#Exercicio D - Cedulas
def cedulas():
    print(">>>>> Exercicio D - Cedulas")
    valorInp = int(input(">> Digite o valor que deseja sacar: R$ "))
    valor = valorInp
    v100 = int(valor / 100)
    valor = valor % 100
    v50 = int(valor / 50)
    valor = valor % 50
    v20 = int(valor / 20)
    valor = valor % 20
    v10 = int(valor / 10)
    valor = valor % 10
    v5 = int(valor / 5)
    valor = valor % 5
    v2 = int(valor / 2)
    valor = valor % 2
    v1 = valor

    print(valorInp)
    print("{} nota(s) de R$ 100,00".format(v100))
    print("{} nota(s) de R$ 50,00".format(v50))
    print("{} nota(s) de R$ 20,00".format(v20))
    print("{} nota(s) de R$ 10,00".format(v10))
    print("{} nota(s) de R$ 5,00".format(v5))
    print("{} nota(s) de R$ 2,00".format(v2))
    print("{} nota(s) de R$ 1,00".format(v1))

#Exercicio E - Soma de Impares dentro de uma lista
def sum_impar():
    print(">>>>> Exercicio E - Soma de Impares dentro de uma lista")
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    Soma = 0
    aux = 0
    #verifica se a sequencia é descrecente e organiza
    if v1>v2:
        aux=v1
        v1=v2
        v2=aux
    #faz o loop de soma
    for i in range(v1+1, v2):
        if i % 2 != 0:
            Soma += i
    print("A soma dos nº ímpares entre {} e {} é {}".format(v1,v2,Soma))

#Exercicio F - Intervalo
def intervalo():
    print(">>>>> Exercicio F - Intervalo")
    qtde = int(input(">> Informe quantas entradas de valores deseja inserir: "))
    inp = 0
    out = 0
    aux = 0
    while aux < qtde:
        var = int(input(">> Digite o valor: "))
        aux +=1
        if (var <10 or var>20):
            out+=1
        else:
            inp+=1

    print("{} in".format(inp))
    print("{} out".format(out))

#Exercicio G - Ordenação Simples
def order_simples():
    #var.sort() - ordena a lista original permanente
    #sorted(var) - ordena a lista temporariamente sem modificar a original
    print(">>>>> Exercicio G - Ordenação Simples")
    vStr = input(">> Digite os valores desejados para ordenar a lista: ").split(" ")
    vInt = []
    for val in vStr: #faz um loop de verificar do primeiro até o ultimo item na lista
        vInt.append(int(val))
    index = sorted(vInt)
    for val in index:
        print(val)
    print("")
    for val in vInt:
        print(val)

#Exercicio H - Tipos de triângulo
def type_trinangulo():
    print(">>>>> Exercicio H - Tipos de triângulo")
    lsString = input(">> Informe 3 valores para verificar que tipo de triângulo é formado: ").split(" ")
    lsFloat = []
    for val in lsString:
        lsFloat.append(float(val))
    lsFloat.sort()
    A=lsFloat[2]
    B=lsFloat[1]
    C=lsFloat[0]
    if (A>=(B+C)):
        print("NÂO FORMA TRIÂNGULO")
    else:
        if (A**2==(B**2+C**2)):
            print("TRIÂNGULO RETÂNGULO")
        if (A**2>(B**2+C**2)):
            print("TRIÂNGULO OBTUSANGULO")
        if (A**2<(B**2+C**2)):
            print("TRIÂNGULO ACUTANGULO")
        if (A==B==C):
            print("TRIÂNGULO EQUILATERO")
        if (A==B or B==C or A==C):
            print("TRIÂNGULO ISOSCELES")

#Exercicio I - Triangulo
def triangulo():
    print(">>>>> Exercicio I - Triângulo")
    lsString = input(">> Informe 3 valores para para calcular área ou perímetro: ").split(" ")
    lsFloat = []
    for val in lsString:
        lsFloat.append(float(val))
    A=lsFloat[0]
    B=lsFloat[1]
    C=lsFloat[2]
    if (A>=B+C or B>=C+A or C>=A+B): # regra existência do triangulo - 1 não pode ser Maior/Igual que a soma dos outros 2
        area = (A + B) * C / 2.0 #area do trapezio - soma dos dois lados multiplicado pela altura / 2
        print("Area = {}".format((area)))
    else:
        perimetro = (A+B+C) #perimetro do triangulo - soma de todos os lados
        print("Perimetro = {}".format((perimetro)))

#Exercicio J - Tempo Jogo
def tempo_jogo():
    print(">>>>> Exercicio J - Tempo de Jogo")
    lsString = input(">> Informe Hora inicial - min inicial / Hora final - min final do jogo: ").split(" ")
    lsInt = []
    for val in lsString:
        lsInt.append(int(val))
    hInicial = lsInt[0]
    mInicial = lsInt[1]
    hFinal = lsInt[2]
    mFinal = lsInt[3]

    if hInicial < hFinal:
        hora = hFinal - hInicial
        if mInicial < mFinal:
            minutos = mFinal - mInicial
        if mInicial > mFinal:
            hora -= 1
            minutos = (60 - mInicial) + mFinal
        if mInicial == mFinal:
            minutos = 0
    if hInicial > hFinal:
        hora = (24 - hInicial) + hFinal
        if mInicial < mFinal:
            minutos = mFinal - mInicial
        if mInicial > mFinal:
            hora -= 1
            minutos = (60 - mInicial) + mFinal
        if mInicial == mFinal:
            minutos = 0
    if hInicial == hFinal:
        if mInicial < mFinal:
            minutos = mFinal - mInicial
            hora = 0
        if mInicial > mFinal:
            minutos = (60 - mInicial) + mFinal
            hora = 23
        if mInicial == mFinal:
            hora = 24
            minutos = 0

    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora, minutos))

main_menu()