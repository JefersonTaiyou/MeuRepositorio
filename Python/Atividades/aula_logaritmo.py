from sympy import symbols
from prettytable import PrettyTable
import math
from fractions import Fraction
import numpy as np
from matplotlib import pyplot as plt

def tabela_graf_log():
    x, y = symbols('x, y')

    a=2
    def f(x):
        return math.log(x, a)

    listx = [str(Fraction(a ** i).limit_denominator()) for i in range(-2, 3)]
    listy = [f(a ** i) for i in range(-2, 3)]
    listxy = [(str(Fraction(a ** i).limit_denominator()),f(a ** i)) for i in range(-2, 3)]

    tabela = PrettyTable()
    tabela.add_column("x",listx)
    tabela.add_column("f(x)",listy)
    tabela.add_column("(x, y))",listxy)
    print(tabela)

def tabela_graf():
    x, y = symbols('x, y')

    a=2
    def f(x):
        return (1+1/x)**x

    listx = [10 ** i for i in range(0, 7)]
    listy = [round(f(10 ** i),7) for i in range(0, 7)]

    tabela = PrettyTable()
    tabela.add_column("x",listx)
    tabela.add_column("f(x)",listy)
    print(tabela)

def grafico():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
    plt.axis([0, 6, 0, 20])  # [xmin, xmax, ymin, ymax]
    plt.show()

def graficos():

    def grafico_linha():
        # 100 valores no intervalo de 0 a 2.
        x = np.linspace(0, 2, num=100)

        # define a legenda e tamanho de linhas
        plt.plot(x, x, label='linear')

        plt.plot(x, x ** 2, label='quadratico', linewidth=5)

        plt.xlabel('x label')
        plt.ylabel('y label')

        plt.title("Gráfico de Linhas Simples")

        # Exibe a legenda e por padrão usa o label de cada plot.
        plt.legend()

        # Configurações do texto
        plt.text(1.00, 1.0, "Cruzamento das Linhas", fontsize=8, horizontalalignment='right')

        plt.show()
    def grafico_pizza():
        vendas = [3000, 2300, 1000, 500]
        labels = ['E-commerce', 'Loja Física', 'e-mail', 'Marketplace']

        # define o nível de separabilidade entre as partes, ordem do vetor representa as partes
        explode = (0.1, 0, 0, 0)

        # define o formato de visualização com saída em 1.1%%, sombras e a separação entre as partes
        plt.pie(vendas, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode)

        # inseri a legenda e a localização da legenda.
        plt.legend(labels, loc=3)

        # define que o gráfico será plotado em circulo
        plt.axis('equal')

        plt.show()
    def grafico_barra_horizontal():
        grupos = ['Produto A', 'Produto B', 'Produto C']
        valores = [1, 10, 100]

        plt.barh(grupos, valores)
        plt.barh(grupos, valores)
        plt.yticks(rotation=45)

        plt.show()
    def grafico_barra_aninhado():
        # Quantidade de vendas para o Produto A
        valores_produto_A = [6, 7, 8, 4, 4]

        # Quantidade de vendas para o Produto B
        valores_produto_B = [3, 12, 3, 4.1, 6]

        # Cria eixo x para produto A e produto B com uma separação de 0.25 entre as barras
        x1 = np.arange(len(valores_produto_A))
        x2 = [x + 0.25 for x in x1]

        # Plota as barras
        plt.bar(x1, valores_produto_A, width=0.25, label='Produto A', color='b')
        plt.bar(x2, valores_produto_B, width=0.25, label='Produto B', color='y')

        # coloca o nome dos meses como label do eixo x
        meses = ['Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        plt.xticks([x + 0.25 for x in range(len(valores_produto_A))], meses)

        # insere uma legenda no gráfico
        plt.legend()
        plt.title("Gráfico Aninhado")
        plt.show()

    def grafico_cores():
        # Define as configurações dos plots
        # Cada plot terá o mesmo tamanho de figuras (10,5)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

        # Dados para cada subplot
        ax1.bar([1, 2, 3], [3, 4, 5], color='#00BFFF')
        ax2.barh([0.5, 1, 2.5], [0, 1, 2], color='#00FF00')

        ax1.set(title="Gráfico de Barras Verticais", xlabel="Eixo x", ylabel=" Eixo y")
        ax2.set(title="Gráfico de Barras Horizontais", xlabel="Eixo x", ylabel="Eixo y")

        plt.show()
    grafico_barra_aninhado()

def aula2109_1():
    x, y = symbols('x, y')

    # Definir a função
    def f(x):
        return x ** 2 - 3 * x
        '''
        return 1 / x ** 2
        return 1 / x
        return (10 * x - 45) / (x - 5)
        '''

    # Analisar próximo de a
    a = 0
    listxe = [(a - 10 ** (-i)) for i in range(1, 5)]
    listye = [round(f(a - 10 ** (-i)), 7) for i in range(1, 5)]
    listxd = [(a + 10 ** (-i)) for i in range(1, 5)]
    listyd = [round(f(a + 10 ** (-i)), 7) for i in range(1, 5)]

    tabelae = PrettyTable()
    tabelae.add_column("x", listxe)
    tabelae.add_column("f(x)", listye)
    print(tabelae)

    tabelad = PrettyTable()
    tabelad.add_column("x", listxd)
    tabelad.add_column("f(x)", listyd)
    print(tabelad)

def aula2109_2():
    x, y = symbols('x, y')

    # Definir a função
    def f(x):
        '''
        return 1 / x **
        '''
        return (10 * x - 45) / (x - 5)

    listxe = [10 ** i for i in range(1, 5)]
    listye = ["{:.8f}".format(f(10 ** i)) for i in range(1, 5)]
    listxd = [-10 ** i for i in range(1, 5)]
    listyd = ["{:.8f}".format(f(-10 ** i)) for i in range(1, 5)]

    tabelae = PrettyTable()
    tabelae.add_column("x", listxe)
    tabelae.add_column("f(x)", listye)
    print(tabelae)

    tabelad = PrettyTable()
    tabelad.add_column("x", listxd)
    tabelad.add_column("f(x)", listyd)
    print(tabelad)

aula2109_2()