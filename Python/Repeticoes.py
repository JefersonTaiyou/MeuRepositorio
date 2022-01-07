import os, traceback
from datetime import datetime

def Comprimir():
    try:
        with open('Arquivo.txt', 'r') as arquivo:
            arq_leitura = open('Arquivo.txt', 'r', encoding='utf-8')
            arq_escrita = open('ArquivoCr.txt', 'w', encoding='utf-8')
            cont = 0
            branco = 0
            dicionario = dict()
            array_palavras = []

            for paragrafo in arq_leitura:
                for linha in paragrafo.split("\n"):
                    for letra in linha.split():
                        if letra not in dicionario.keys():
                            cont += 1
                            dicionario[letra] = f'd{cont}'
                            array_palavras.append(letra)
                        else:
                            array_palavras.append(dicionario.get(letra))
                    for letra in array_palavras:
                        if array_palavras.index(letra) == 0:
                            arq_escrita.write(f'{letra} ')
                        else:
                            arq_escrita.write(f'{letra}d{branco}')

            arq_leitura.close()
            arq_escrita.close()
            data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{data_hora} Compressão de repetições compilado com sucesso\n')
                arquivo.close()

    except OSError:
        err = traceback.format_exc()
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Compressão de repetições - OS Error:\n {err}\n\n')
            arquivo.close()

    except ValueError:
        err = traceback.format_exc()
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Compressão de repetições - Value Error:\n {err}\n\n')
            arquivo.close()

    except BaseException:
        err = traceback.format_exc()
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Compressão de repetições - Unexpected:\n {err}\n\n')
            arquivo.close()
        raise

def Descomprimir():
    try:
        with open('ArquivoCr.txt', 'r') as arquivo:
            arq_leitura = open('ArquivoCr.txt', 'r', encoding='utf-8')
            arq_escrita = open('ArquivoDr.txt', 'w', encoding='utf-8')
            cont = 0
            dicionario = dict()
            array_palavras = []

            for paragrafo in arq_leitura:
                for linha in paragrafo.split("\n"):
                    for palavra in linha.split():
                        for letra in palavra.split("d0"):
                            if letra not in dicionario.keys():
                                if letra not in dicionario.values():
                                    cont += 1
                                    dicionario[letra] = f'd{cont}'
                                    array_palavras.append(letra)
                            if letra in dicionario.values():
                                listagem = list(dicionario.keys())
                                if letra.find('d') == 0:
                                    if letra.split('d')[-1].isnumeric():
                                        v1 = letra.split('d')[-1]
                                        v2 = int(v1) - 1
                                        if v2 <= len(listagem):
                                            array_palavras.append(listagem[v2])

            for letra in array_palavras:
                arq_escrita.write(f'{letra} ')

            arq_leitura.close()
            arq_escrita.close()
            data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{data_hora} Descompressão de repetições compilado com sucesso\n\n')
                arquivo.close()

    except OSError:
        err = traceback.format_exc()
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Descompressão de repetições - OS Error:\n {err}\n\n')
            arquivo.close()

    except ValueError:
        err = traceback.format_exc()
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Descompressão de repetições - Value Error:\n {err}\n\n')
            arquivo.close()

    except BaseException:
        err = traceback.format_exc()
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Descompressão de repetições - Unexpected:\n {err}\n\n')
            arquivo.close()
        raise

def main():
    Comprimir()
    Descomprimir()

if __name__ == '__main__':
    main()