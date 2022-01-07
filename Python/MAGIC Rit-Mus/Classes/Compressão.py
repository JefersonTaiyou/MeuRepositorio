# -*- coding: utf-8 -*-
import hashlib
import os

from cryptography.fernet import Fernet

# abrindo a chave
with open('Dados/filekey.key', 'rb') as filekey:
        if filekey == 'xxx':
            key = Fernet.generate_key()
            with open('Dados/filekey.key', 'wb') as filekey:
                filekey.write(key)
        else:
            key = filekey.read()

print(key,len(key))
# usando a chave gerada
fernet = Fernet(key)

# abrindo o arquivo original para criptografar
with open('Dados/Ranking.dat', 'rb') as file:
    original = file.read()

# criptografar o arquivo
encrypted = fernet.encrypt(original)

# abrir o arquivo no modo de gravação e
# gravar os dados criptografados
with open('Dados/encryptedRanking.dat', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

# usando a chave
fernet = Fernet(key)

# abrindo o arquivo criptografado
with open('Dados/encryptedRanking.dat', 'rb') as enc_file:
    encrypted = enc_file.read()

# descriptografando o arquivo
decrypted = fernet.decrypt(encrypted)

# abrindo o arquivo no modo de gravação e
# gravando os dados descriptografados
with open('Dados/decryptedRanking.dat', 'wb') as dec_file:
    dec_file.write(decrypted)

print(os.stat('Dados/Ranking.dat').st_size)
print(os.stat('Dados/encryptedRanking.dat').st_size)
print(os.stat('Dados/decryptedRanking.dat').st_size)

# SITE pra descodificar hash
# https://crackstation.net/

dicionario ={"Rank1":"","Rank2":"",
             "Rank3":"", "Rank4":"",
             "Rank5":""}

'''rank = [linha.replace('\n','') for linha in open('Dados/Ranking.dat', 'r', encoding='utf-8')]
rank = [linha.split() for linha in rank]
order = sorted([[x,int(y),int(z)] for x,y,z in rank], key=lambda item: item[1],reverse=True)

for alt in range(len(dicionario)):
    key=f'Rank{alt+1}'
    dicionario[key]=order[alt]

print(order[0][0],order[1][0],order[2][0],order[3][0],order[4][0],order[5][0])


print(hashlib.md5(str(f'{order[0][0]} {order[1][0]}').encode('utf-8')).hexdigest())
print(hashlib.md5(str(order[4][0]).encode('utf-8')).hexdigest())

print(hashlib.md5(str(order[1][0]).encode('utf-8')).hexdigest())
print(hashlib.md5(str(order[3][0]).encode('utf-8')).hexdigest())

print(hashlib.md5(str(order[2][0]).encode('utf-8')).hexdigest())
print(hashlib.md5(str(order[5][0]).encode('utf-8')).hexdigest())'''

'''
print(hashlib.sha1(str(order[1][1]).encode('utf-8')).hexdigest())
print(hashlib.sha224(str(order[1][1]).encode('utf-8')).hexdigest())
print(hashlib.sha256(str(order[1][1]).encode('utf-8')).hexdigest())
print(hashlib.sha384(str(order[1][1]).encode('utf-8')).hexdigest())
print(hashlib.sha512(str(order[1][1]).encode('utf-8')).hexdigest()) # [:10]
'''
