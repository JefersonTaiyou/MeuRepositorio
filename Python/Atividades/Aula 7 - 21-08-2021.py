# -*- coding: utf-8 -*-

entrada = int(input("ENTRADA: "))
print(">> SAIDA {}".format(entrada))

# lista.insert(1,99) - onde 1 é a posição que vc deseja salvar e o 99 é o valor que será adicionado
# del lista[2] - deleta o valor que está no index(2)

'''
lista pode ser modificada - []
tupla não pode ser - ()

tupla=('A','B','C','D')
print(tupla[1:3]) = B,C - conta até a ultima posição sem mostra-la

desempacotamento de tupla precisa ser completo,
não da pra descompactar parcialmente
'''

'''
DICIONARIO DE DADOS

ddd={"I":"Ingrid", "J":"Jeferson", "N":"Natan"}

NÂO PODEM REPETIR CHAVES no dicionario de dados
mas chaves diferentes podem ter valores repetidos

NÂO PODE:
ddd={"I":"Ingrid", "I":"Jeferson"}

PODE:
ddd={"I":"Ingrid", "J":"Ingrid"}

print(ddd) #chamando todas as chaves e valores delas
print(ddd.items()) #retorna as keys e values em lista
print(ddd.keys()) #retorna apenas as keys em lista
print(ddd.values())

nome = ddd['I']

MODIFICAR VALORES DE DICIONARIO:

ddd['I'] = 'Thiago'

for x in ddd:
    print(x)

var in ddd - verifica se a variavel existe como key no dicionario
if var in ddd:
    print()
else:
    print()


#>>>>> padrão pep8.org e type annotations - utilizado para polimento de código
#>>>>> exemplo a seguir:

    #define o tipo de dados de entrada e o tipo de retorno
def sum_two_numbers(a: int, b: int) -> int:
    #retorna a soma de a e b
    return a + b
    
        # define os tipos dos dados do dicionario
                #define a key como str
                #define o valor como int
result: Mapping[str, int] = {
    "result10": sum_two_numbers(5,5),
    "result20": sum_two_numbers(15,15)
}

context managers
usar o padrão de funcoes: tudo minusculo separado com underline ex: soma_num_primo
usar exceptions para tratar erros
'''

