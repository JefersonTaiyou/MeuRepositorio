import os, traceback
from datetime import datetime

def Comprimir():
    try:
        with open('Arquivo.txt', 'r') as arquivo:
            arq_leitura = open('Arquivo.txt', 'r', encoding='utf-8')
            arq_escrita = open('ArquivoCb.txt', 'w', encoding='utf-8')
            cont = 0
            array_cont = []

            for linha in arq_leitura:
                for letra in linha:
                    if letra.isspace():
                        cont += 1
                    else:
                        if cont != 0:
                            array_cont.append(f'v{cont}')
                        cont = 0
                        array_cont.append(letra)

                for letra in array_cont:
                    arq_escrita.write(f'{letra}')

                arq_leitura.close()
                arq_escrita.close()
            data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{data_hora} Compressão de brancos compilado com sucesso\n')
                arquivo.close()

    except OSError:
        err = traceback.format_exc()
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Compressão de brancos - OS Error:\n {err}\n\n')
            arquivo.close()

    except ValueError:
        err = traceback.format_exc()
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Compressão de brancos - Value Error:\n {err}\n\n')
            arquivo.close()

    except BaseException:
        err = traceback.format_exc()
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Compressão de brancos - Unexpected:\n {err}\n\n')
            arquivo.close()
        raise

def Descomprimir():
    try:
        with open('ArquivoCb.txt', 'r') as arquivo:
            arq_leitura = open('ArquivoCb.txt', 'r', encoding='utf-8')
            arq_escrita = open('ArquivoDb.txt', 'w', encoding='utf-8')
            array_total = []

            for linha in arq_leitura:
                for letra in linha:
                    array_total.append(letra)
                    if len(array_total) > 4:
                        penultimoCaracter = str(array_total[-2])
                        antePenultimoCaracter = str(array_total[-3])
                        anteAntePenultimoCaracter = str(array_total[-4])

                        if not array_total[-1].isnumeric():
                            if anteAntePenultimoCaracter == 'v' and antePenultimoCaracter.isnumeric():
                                if not penultimoCaracter.isnumeric():
                                    cont = array_total[-3]
                                    array_total[-4] = str(array_total[-4]).replace('v', ' ')
                                    array_total[-3] = str(array_total[-3]).replace(antePenultimoCaracter,
                                                                                   ' ' * (int(cont) - 1))
                                else:
                                    cont = array_total[-3] + array_total[-2]
                                    array_total[-4] = str(array_total[-4]).replace('v', ' ')
                                    array_total[-3] = str(array_total[-3]).replace(antePenultimoCaracter,
                                                                                   ' ' * (int(cont) - 2))
                                    array_total[-2] = str(array_total[-2]).replace(penultimoCaracter, ' ')
                        else:
                            if anteAntePenultimoCaracter == 'v' and antePenultimoCaracter.isnumeric():
                                cont = array_total[-3]
                                array_total[-4] = str(array_total[-4]).replace('v', ' ')
                                array_total[-3] = str(array_total[-3]).replace(antePenultimoCaracter,
                                                                               ' ' * (int(cont) - 1))

            for letra in array_total:
                arq_escrita.write(f'{letra}')

            arq_leitura.close()
            arq_escrita.close()
            data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{data_hora} Descompressão de brancos compilado com sucesso\n\n')
                arquivo.close()

    except OSError:
        err = traceback.format_exc()
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Descompressão de brancos - OS Error:\n {err}\n\n')
            arquivo.close()

    except ValueError:
        err = traceback.format_exc()
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Descompressão de brancos - Value Error:\n {err}\n\n')
            arquivo.close()

    except BaseException:
        err = traceback.format_exc()
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Descompressão de brancos - Unexpected:\n {err}\n\n')
            arquivo.close()
        raise

def main():
    Comprimir()
    Descomprimir()

if __name__ == '__main__':
    main()