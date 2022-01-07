# -*- coding: utf-8 -*-
import pygame,traceback, sys
from datetime import datetime
from pygame.locals import *

from Classes import app_data
from Classes.Opcoes import drwText
from Classes.app_data import __formas__, sfxSelect

try:
    LARGURA = 1280
    ALTURA = 710
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('MAGIC Rit-Mus')  # defino o nome da barra de titulo
    icon = pygame.image.load('Imagens/1x/Icone.png')
    icon = pygame.transform.scale(icon, (46, 32))
    pygame.display.set_icon(icon)

    relogio = pygame.time.Clock()

    def skin(forma, skin, level):
            app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[forma], level, skin), (600, 290))

    def diminui_notas():
        global tamanho_colisao_x, tamanho_colisao_y
        tamanho_colisao_x, tamanho_colisao_y = 30,25

    def aumenta_notas():
        global tamanho_colisao_x, tamanho_colisao_y
        tamanho_colisao_x, tamanho_colisao_y = 45, 30

    def call_game():

        running = True
        duracao_vermelho = 0
        duracao_verde = 0
        duracao_azul = 0
        duracao_branco = 0
        clock = 0
        pontos = 0
        streak = 0

        y_linhas = 50
        x_linhas = 120

        japontuouvermelho_check = 0
        japontuouverde_check = 0
        japontuouazul_check = 0
        japontuoubranco_check = 0

        PRETO = (0, 0, 0)
        BRANCO = (255, 255, 255)
        VERMELHO = (255, 0, 0)
        VERDE = (0, 255, 0)
        AZUL = (0, 0, 255)

        y_notavermelha1 = -30
        y_notavermelha2 = -30
        y_notavermelha3 = -30
        y_notavermelha4 = -30

        y_notaverde1 = -30
        y_notaverde2 = -30
        y_notaverde3 = -30
        y_notaverde4 = -30

        y_notaazul1 = -30
        y_notaazul2 = -30
        y_notaazul3 = -30
        y_notaazul4 = -30

        y_notabranca1 = -30
        y_notabranca2 = -30
        y_notabranca3 = -30
        y_notabranca4 = -30

        agoravermelho1 = 0
        agoravermelho2 = 0
        agoravermelho3 = 0
        agoravermelho4 = 0

        agoraverde1 = 0
        agoraverde2 = 0
        agoraverde3 = 0
        agoraverde4 = 0

        agoraazul1 = 0
        agoraazul2 = 0
        agoraazul3 = 0
        agoraazul4 = 0

        agorabranco1 = 0
        agorabranco2 = 0
        agorabranco3 = 0
        agorabranco4 = 0

        VELOCIDADE = 3

        tamanho_colisao_vermelho_x = 30
        tamanho_colisao_vermelho_y = 25
        tamanho_colisao_verde_x = 30
        tamanho_colisao_verde_y = 25
        tamanho_colisao_azul_x = 30
        tamanho_colisao_azul_y = 25
        tamanho_colisao_branco_x = 30
        tamanho_colisao_branco_y = 25

        fill_colisao_vermelho_x = 3
        fill_colisao_verde_x = 3
        fill_colisao_azul_x = 3
        fill_colisao_branco_x = 3

        setavermelha = pygame.image.load('Imagens/Setas/Ativo119.png')
        setavermelha = pygame.transform.scale(setavermelha, (60, 60))
        setaverde = pygame.image.load('Imagens/Setas/Ativo116.png')
        setaverde = pygame.transform.scale(setaverde, (60, 60))
        setaazul = pygame.image.load('Imagens/Setas/Ativo117.png')
        setaazul = pygame.transform.scale(setaazul, (60, 60))
        setabranca = pygame.image.load('Imagens/Setas/Ativo118.png')
        setabranca = pygame.transform.scale(setabranca, (60, 60))

        ponto_check_vermelho = 0
        ponto_check_verde = 0
        ponto_check_azul = 0
        ponto_check_branco= 0

        imagem_fundo = pygame.image.load('Imagens/BG/Ativo168.png').convert()
        imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))

        erros = 0

        while running:
            pygame.init()
            clock = clock+1
            duracao_vermelho = duracao_vermelho-1
            duracao_verde = duracao_verde - 1
            duracao_azul = duracao_azul - 1
            duracao_branco = duracao_branco - 1
            tela.fill(PRETO)
            relogio.tick(100)
            pts = f'{pontos}'
            strk = f'x{streak}'
            if clock == 180:
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.load('Sounds/01.mp3')
                pygame.mixer.music.play(0)

            tela.blit(imagem_fundo, (0, 0))
            pygame.draw.line(tela,BRANCO,(120*1,0),(120*1,ALTURA))
            pygame.draw.line(tela,BRANCO,(120*2,0),(120*2,ALTURA))
            pygame.draw.line(tela,BRANCO,(120*3,0),(120*3,ALTURA))
            pygame.draw.line(tela,BRANCO,(120*4,0),(120*4,ALTURA))
            linha1 = pygame.draw.line(tela, BRANCO, (x_linhas,y_linhas-50), (x_linhas*4,y_linhas-50))
            linha2 = pygame.draw.line(tela, BRANCO, (x_linhas, y_linhas), (x_linhas * 4, y_linhas))
            linha3 = pygame.draw.line(tela, BRANCO, (x_linhas, (y_linhas+50)), (x_linhas * 4, (y_linhas+50)))
            linha4 = pygame.draw.line(tela, BRANCO, (x_linhas, y_linhas+100), (x_linhas * 4, y_linhas+100))
            linha5 = pygame.draw.line(tela, BRANCO, (x_linhas, y_linhas+150), (x_linhas * 4, y_linhas+150))
            linha6 = pygame.draw.line(tela, BRANCO, (x_linhas, y_linhas+200), (x_linhas * 4, y_linhas+200))
            linha7 = pygame.draw.line(tela, BRANCO, (x_linhas, y_linhas+250), (x_linhas * 4, y_linhas+250))
            linha8 = pygame.draw.line(tela, BRANCO, (x_linhas, y_linhas+300), (x_linhas * 4, y_linhas+300))
            linha9 = pygame.draw.line(tela, BRANCO, (x_linhas, y_linhas + 350), (x_linhas * 4, y_linhas + 350))
            linha10 = pygame.draw.line(tela, BRANCO, (x_linhas, y_linhas + 400), (x_linhas * 4, y_linhas + 400))
            linha11 = pygame.draw.line(tela, BRANCO, (x_linhas, y_linhas + 450), (x_linhas * 4, y_linhas + 450))
            linha12 = pygame.draw.line(tela, BRANCO, (x_linhas, y_linhas + 500), (x_linhas * 4, y_linhas + 500))
            linha13 = pygame.draw.line(tela, BRANCO, (x_linhas, y_linhas + 550), (x_linhas * 4, y_linhas + 550))
            linha14 = pygame.draw.line(tela, BRANCO, (x_linhas, y_linhas + 600), (x_linhas * 4, y_linhas + 600))

            colisao_notas = pygame.draw.line(tela, BRANCO, (0, ALTURA-30), (LARGURA, ALTURA-30))
            colisao_notavermelha = pygame.draw.ellipse(tela, VERMELHO, (106,ALTURA-42, tamanho_colisao_vermelho_x, tamanho_colisao_vermelho_y),fill_colisao_vermelho_x)
            colisao_notaverde = pygame.draw.ellipse(tela, VERDE, (226, ALTURA - 42, tamanho_colisao_verde_x, tamanho_colisao_verde_y),fill_colisao_verde_x)
            colisao_notaazul = pygame.draw.ellipse(tela, AZUL, (346, ALTURA - 42, tamanho_colisao_azul_x, tamanho_colisao_azul_y),fill_colisao_azul_x)
            colisao_notabranca = pygame.draw.ellipse(tela, BRANCO, (466, ALTURA - 42, tamanho_colisao_branco_x, tamanho_colisao_branco_y),fill_colisao_branco_x)
            y_linhas = y_linhas + VELOCIDADE
            if y_linhas > 99:
                y_linhas = 50
                x_linhas = 120
            if duracao_vermelho == 0:
                fill_colisao_vermelho_x = 3
            if duracao_verde == 0:
                fill_colisao_verde_x = 3
            if duracao_azul == 0:
                fill_colisao_azul_x = 3
            if duracao_branco == 0:
                fill_colisao_branco_x = 3
            notavermelha1 = tela.blit(setavermelha,(120-30, y_notavermelha1))
            notavermelha2 = tela.blit(setavermelha,(120-30, y_notavermelha2))
            notavermelha3 = tela.blit(setavermelha,(120-30, y_notavermelha3))
            notavermelha4 = tela.blit(setavermelha,(120-30, y_notavermelha4))

            notaverde1 = tela.blit(setaverde,(240-30, y_notaverde1))
            notaverde2 = tela.blit(setaverde,(240-30, y_notaverde2))
            notaverde3 = tela.blit(setaverde,(240-30, y_notaverde3))
            notaverde4 = tela.blit(setaverde,(240-30, y_notaverde4))

            notaazul1 = tela.blit(setaazul,(360-30, y_notaazul1))
            notaazul2 = tela.blit(setaazul,(360-30, y_notaazul2))
            notaazul3 = tela.blit(setaazul,(360-30, y_notaazul3))
            notaazul4 = tela.blit(setaazul,(360-30, y_notaazul4))

            notabranca1 = tela.blit(setabranca,(480-30, y_notabranca1))
            notabranca2 = tela.blit(setabranca,(480-30, y_notabranca2))
            notabranca3 = tela.blit(setabranca,(480-30, y_notabranca3))
            notabranca4 = tela.blit(setabranca,(480-30, y_notabranca4))
                                ##INSERÇÃO DE NOTAS
                ##intro
            if clock == 150:
                agoravermelho1 = 1
            if clock == 675:
                agoravermelho2 = 1
            if clock == 725:
                agoravermelho3 = 1
            if clock == 775:
                agoravermelho4 = 1
            if clock == 1200:
                agoravermelho1 = 1
            if clock == 1325:
                agoravermelho2 = 1
            if clock == 2100:
                agoravermelho3 = 1
            if clock == 2375:
                agoravermelho4 = 1
            if clock == 2500:
                agoravermelho1 = 1
            if clock == 3975:
                agoravermelho2 = 1
            if clock == 4010:
                agoravermelho3 = 1
            if clock == 4075:
                agoravermelho4 = 1
            if clock == 4135:
                agoravermelho1 = 1
            if clock == 4200:
                agoravermelho2 = 1
            if clock == 6301:
                agoravermelho3 = 1
            if clock == 6344:
                agoravermelho4 = 1
            if clock == 6447:
                agoravermelho1 = 1
            if clock == 6515:
                agoravermelho2 = 1
            if clock == 7407:
                agoravermelho3 = 1
            if clock == 7955:
                agoravermelho4 = 1
            if clock == 8504:
                agoravermelho1 = 1
            if clock == 8521:
                agoravermelho2 = 1
            if clock == 9052:
                agoravermelho3 = 1
            if clock == 9070:
                agoravermelho4 = 1
            if clock == 9601:
                agoravermelho1 = 1
            if clock == 10424:
                agoravermelho2 = 1
            if clock == 10698:
                agoravermelho3 = 1
            if clock == 10732:
                agoravermelho4 = 1
            if clock == 10767:
                agoravermelho1 = 1
            if clock == 11521:
                agoravermelho2 = 1
            if clock == 11555:
                agoravermelho3 = 1
            if clock == 11590:
                agoravermelho4 = 1
            if clock == 12070:
                agoravermelho1 = 1
            if clock == 12104:
                agoravermelho2 = 1
            if clock == 12138:
                agoravermelho3 = 1
            if clock == 11590:
                agoravermelho4 = 1
            if clock == 12070:
                agoravermelho1 = 1
            if clock == 12104:
                agoravermelho2 = 1
            if clock == 12344:
                agoravermelho3 = 1
            if clock == 12378:
                agoravermelho4 = 1
            if clock == 12412:
                agoravermelho1 = 1
            if clock == 13412:
                agoravermelho2 = 1
            if clock == 13852:
                agoravermelho3 = 1
            if clock == 14264:
                agoravermelho4 = 1
            if clock == 15087:
                agoravermelho1 = 1
            if clock == 15104:
                agoravermelho2 = 1
            if clock == 16184:
                agoravermelho3 = 1
            if clock == 16201:
                agoravermelho4 = 1
            if clock == 16218:
                agoravermelho1 = 1
            if clock == 16235:
                agoravermelho2 = 1

            if clock == 275:
                agoraverde1 = 1
            if clock == 1450:
                agoraverde2 = 1
            if clock == 1850:
                agoraverde3 = 1
            if clock == 3190:
                agoraverde4 = 1
            if clock == 3210:
                agoraverde1 = 1
            if clock == 3715:
                agoraverde2 = 1
            if clock == 3735:
                agoraverde3 = 1
            if clock == 4499:
                agoraverde4 = 1
            if clock == 4533:
                agoraverde1 = 1
            if clock == 4599:
                agoraverde2 = 1
            if clock == 4666:
                agoraverde3 = 1
            if clock == 4733:
                agoraverde4 = 1
            if clock == 5761:
                agoraverde1 = 1
            if clock == 6035:
                agoraverde2 = 1
            if clock == 6858:
                agoraverde3 = 1
            if clock == 6892:
                agoraverde4 = 1
            if clock == 6995:
                agoraverde1 = 1
            if clock == 7064:
                agoraverde2 = 1
            if clock == 7544:
                agoraverde3 = 1
            if clock == 7612:
                agoraverde4 = 1
            if clock == 8092:
                agoraverde1 = 1
            if clock == 8161:
                agoraverde2 = 1
            if clock == 9875:
                agoraverde3 = 1
            if clock == 10150:
                agoraverde4 = 1
            if clock == 10424:
                agoraverde1 = 1
            if clock == 10835:
                agoraverde2 = 1
            if clock == 10870:
                agoraverde3 = 1
            if clock == 10939:
                agoraverde4 = 1
            if clock == 11246:
                agoraverde1 = 1
            if clock == 11281:
                agoraverde2 = 1
            if clock == 11315:
                agoraverde3 = 1
            if clock == 11658:
                agoraverde4 = 1
            if clock == 11692:
                agoraverde1 = 1
            if clock == 11727:
                agoraverde2 = 1
            if clock == 12618:
                agoraverde3 = 1
            if clock == 12652:
                agoraverde4 = 1
            if clock == 12687:
                agoraverde1 = 1
            if clock == 13578:
                agoraverde2 = 1
            if clock == 14127:
                agoraverde3 = 1
            if clock == 14538:
                agoraverde4 = 1
            if clock == 14555:
                agoraverde1 = 1
            if clock == 15635:
                agoraverde2 = 1
            if clock == 15653:
                agoraverde3 = 1

            if clock == 412:
                agoraazul1 = 1
            if clock == 1590:
                agoraazul2 = 1
            if clock == 1975:
                agoraazul3 = 1
            if clock == 2920:
                agoraazul4 = 1
            if clock == 2940:
                agoraazul1 = 1
            if clock == 3450:
                agoraazul2 = 1
            if clock == 3470:
                agoraazul3 = 1
            if clock == 4233:
                agoraazul4 = 1
            if clock == 4266:
                agoraazul1 = 1
            if clock == 4325:
                agoraazul2 = 1
            if clock == 4390:
                agoraazul3 = 1
            if clock == 4456:
                agoraazul4 = 1
            if clock == 5487:
                agoraazul1 = 1
            if clock == 7132:
                agoraazul2 = 1
            if clock == 7167:
                agoraazul3 = 1
            if clock == 7270:
                agoraazul4 = 1
            if clock == 7338:
                agoraazul1 = 1
            if clock == 7818:
                agoraazul2 = 1
            if clock == 7887:
                agoraazul3 = 1
            if clock == 8367:
                agoraazul4 = 1
            if clock == 8435:
                agoraazul1 = 1
            if clock == 10150:
                agoraazul2 = 1
            if clock == 10972:
                agoraazul3 = 1
            if clock == 11007:
                agoraazul4 = 1
            if clock == 11041:
                agoraazul1 = 1
            if clock == 11384:
                agoraazul2 = 1
            if clock == 11412:
                agoraazul3 = 1
            if clock == 11452:
                agoraazul4 = 1
            if clock == 11795:
                agoraazul1 = 1
            if clock == 11829:
                agoraazul2 = 1
            if clock == 11864:
                agoraazul3 = 1
            if clock == 12481:
                agoraazul4 = 1
            if clock == 12515:
                agoraazul1 = 1
            if clock == 12549:
                agoraazul2 = 1
            if clock == 12812:
                agoraazul3 = 1
            if clock == 12830:
                agoraazul4 = 1
            if clock == 15910:
                agoraazul1 = 1
            if clock == 15927:
                agoraazul2 = 1

            if clock == 537:
                agorabranco1 = 1
            if clock == 925:
                agorabranco2 = 1
            if clock == 975:
                agorabranco3 = 1
            if clock == 1025:
                agorabranco4 = 1
            if clock == 1200:
                agorabranco1 = 1
            if clock == 1725:
                agorabranco2 = 1
            if clock == 2250:
                agorabranco3 = 1
            if clock == 2650:
                agorabranco4 = 1
            if clock == 2775:
                agorabranco1 = 1
            if clock == 4766:
                agorabranco1 = 1
            if clock == 4799:
                agorabranco2 = 1
            if clock == 4866:
                agorabranco3 = 1
            if clock == 4933:
                agorabranco4 = 1
            if clock == 4999:
                agorabranco1 = 1
            if clock == 5213:
                agorabranco2 = 1
            if clock == 6584:
                agorabranco3 = 1
            if clock == 6618:
                agorabranco4 = 1
            if clock == 6721:
                agorabranco1 = 1
            if clock == 6790:
                agorabranco2 = 1
            if clock == 7681:
                agorabranco3 = 1
            if clock == 8229:
                agorabranco4 = 1
            if clock == 8778:
                agorabranco1 = 1
            if clock == 8795:
                agorabranco2 = 1
            if clock == 9326:
                agorabranco3 = 1
            if clock == 9344:
                agorabranco4 = 1
            if clock == 9601:
                agorabranco1 = 1
            if clock == 9875:
                agorabranco2 = 1
            if clock == 11109:
                agorabranco3 = 1
            if clock == 11144:
                agorabranco4 = 1
            if clock == 11178:
                agorabranco1 = 1
            if clock == 11932:
                agorabranco2 = 1
            if clock == 11967:
                agorabranco3 = 1
            if clock == 12001:
                agorabranco4 = 1
            if clock == 12207:
                agorabranco1 = 1
            if clock == 12241:
                agorabranco2 = 1
            if clock == 12275:
                agorabranco3 = 1
            if clock == 12755:
                agorabranco4 = 1
            if clock == 12789:
                agorabranco1 = 1
            if clock == 12824:
                agorabranco2 = 1
            if clock == 13715:
                agorabranco3 = 1
            if clock == 13990:
                agorabranco4 = 1
            if clock == 14401:
                agorabranco1 = 1
            if clock == 15361:
                agorabranco2 = 1
            if clock == 15378:
                agorabranco3 = 1
            if clock == 16458:
                agorabranco4 = 1
            if clock == 16476:
                agorabranco1 = 1
            if clock == 16493:
                agorabranco2 = 1
            if clock == 16510:
                agorabranco3 = 1

                #---

            if agoravermelho1 == 1:
                y_notavermelha1 = y_notavermelha1+VELOCIDADE
            if agoravermelho2 == 1:
                y_notavermelha2 = y_notavermelha2+VELOCIDADE
            if agoravermelho3 == 1:
                y_notavermelha3 = y_notavermelha3+VELOCIDADE
            if agoravermelho4 == 1:
                y_notavermelha4 = y_notavermelha4+VELOCIDADE

            if agoraverde1 == 1:
                y_notaverde1 = y_notaverde1+VELOCIDADE
            if agoraverde2 == 1:
                y_notaverde2 = y_notaverde2+VELOCIDADE
            if agoraverde3 == 1:
                y_notaverde3 = y_notaverde3+VELOCIDADE
            if agoraverde4 == 1:
                y_notaverde4 = y_notaverde4+VELOCIDADE

            if agoraazul1 == 1:
                y_notaazul1 = y_notaazul1+VELOCIDADE
            if agoraazul2 == 1:
                y_notaazul2 = y_notaazul2+VELOCIDADE
            if agoraazul3 == 1:
                y_notaazul3 = y_notaazul3+VELOCIDADE
            if agoraazul4 == 1:
                y_notaazul4 = y_notaazul4+VELOCIDADE

            if agorabranco1 == 1:
                y_notabranca1 = y_notabranca1+VELOCIDADE
            if agorabranco2 == 1:
                y_notabranca2 = y_notabranca2+VELOCIDADE
            if agorabranco3 == 1:
                y_notabranca3 = y_notabranca3+VELOCIDADE
            if agorabranco4 == 1:
                y_notabranca4 = y_notabranca4+VELOCIDADE


            if y_notavermelha1>ALTURA and ponto_check_vermelho == 0:
                japontuouvermelho_check = 0
                pontos = pontos - 100
                streak=0
                y_notavermelha1=-30
                agoravermelho1=0
                erros = erros + 1
            elif y_notavermelha1>ALTURA and ponto_check_vermelho == 1:
                japontuouvermelho_check = 0
                ponto_check_vermelho = 0
                y_notavermelha1=-30
                agoravermelho1=0
            if y_notavermelha2>ALTURA and ponto_check_vermelho == 0:
                japontuouvermelho_check = 0
                streak = 0
                pontos = pontos - 100
                y_notavermelha2=-30
                agoravermelho2=0
                erros = erros + 1
            elif y_notavermelha2>ALTURA and ponto_check_vermelho == 1:
                japontuouvermelho_check = 0
                ponto_check_vermelho = 0
                y_notavermelha2=-30
                agoravermelho2=0
            if y_notavermelha3>ALTURA and ponto_check_vermelho == 0:
                japontuouvermelho_check = 0
                streak = 0
                pontos = pontos - 100
                y_notavermelha3=-30
                agoravermelho3=0
                erros = erros + 1
            elif y_notavermelha3>ALTURA and ponto_check_vermelho == 1:
                japontuouvermelho_check = 0
                ponto_check_vermelho = 0
                y_notavermelha3=-30
                agoravermelho3=0
            if y_notavermelha4>ALTURA and ponto_check_vermelho == 0:
                japontuouvermelho_check = 0
                streak = 0
                pontos = pontos - 100
                y_notavermelha4=-30
                agoravermelho4=0
                erros = erros + 1
            elif y_notavermelha4>ALTURA and ponto_check_vermelho == 1:
                japontuouvermelho_check = 0
                ponto_check_vermelho = 0
                y_notavermelha4=-30
                agoravermelho4=0

            if y_notaverde1>ALTURA and ponto_check_verde == 0:
                japontuouverde_check = 0
                streak = 0
                pontos = pontos - 100
                y_notaverde1=-30
                agoraverde1=0
                erros = erros + 1
            elif y_notaverde1>ALTURA and ponto_check_verde == 1:
                japontuouverde_check = 0
                ponto_check_verde = 0
                y_notaverde1=-30
                agoraverde1=0
            if y_notaverde2>ALTURA and ponto_check_verde == 0:
                japontuouverde_check = 0
                streak = 0
                pontos = pontos - 100
                y_notaverde2=-30
                agoraverde2=0
                erros = erros + 1
            elif y_notaverde2>ALTURA and ponto_check_verde == 1:
                japontuouverde_check = 0
                ponto_check_verde = 0
                y_notaverde2=-30
                agoraverde2=0
            if y_notaverde3>ALTURA and ponto_check_verde == 0:
                japontuouverde_check = 0
                streak = 0
                pontos = pontos - 100
                y_notaverde3=-30
                agoraverde3=0
                erros = erros + 1
            elif y_notaverde3>ALTURA and ponto_check_verde == 1:
                japontuouverde_check = 0
                ponto_check_verde = 0
                y_notaverde3=-30
                agoraverde3=0
            if y_notaverde4>ALTURA and ponto_check_verde == 0:
                japontuouverde_check = 0
                streak = 0
                pontos = pontos - 100
                y_notaverde4=-30
                agoraverde4=0
                erros = erros + 1
            elif y_notaverde4>ALTURA and ponto_check_verde == 1:
                japontuouverde_check = 0
                ponto_check_verde = 0
                y_notaverde4=-30
                agoraverde4=0

            if y_notaazul1>ALTURA and ponto_check_azul == 0:
                japontuouazul_check = 0
                streak = 0
                pontos = pontos - 100
                y_notaazul1=-30
                agoraazul1=0
                erros = erros + 1
            elif y_notaazul1>ALTURA and ponto_check_azul == 1:
                japontuouazul_check = 0
                ponto_check_azul = 0
                y_notaazul1=-30
                agoraazul1=0
            if y_notaazul2>ALTURA  and ponto_check_azul == 0:
                japontuouazul_check = 0
                streak = 0
                pontos = pontos - 100
                erros = erros +1
                y_notaazul2=-30
                agoraazul2=0
                erros = erros + 1
            elif y_notaazul2>ALTURA and ponto_check_azul == 1:
                japontuouazul_check = 0
                ponto_check_azul=0
                y_notaazul2=-30
                agoraazul2=0
            if y_notaazul3>ALTURA and ponto_check_azul == 0:
                japontuouazul_check = 0
                streak = 0
                pontos = pontos - 100
                y_notaazul3=-30
                agoraazul3=0
                erros = erros + 1
            elif y_notaazul3>ALTURA and ponto_check_azul == 1:
                japontuouazul_check = 0
                ponto_check_azul = 0
                y_notaazul3=-30
                agoraazul3=0
            if y_notaazul4>ALTURA and ponto_check_azul == 0:
                japontuouazul_check = 0
                streak = 0
                pontos = pontos - 100
                y_notaazul4=-30
                agoraazul4=0
                erros = erros + 1
            elif y_notaazul4>ALTURA and ponto_check_azul == 1:
                japontuouazul_check = 0
                ponto_check_azul = 0
                y_notaazul4=-30
                agoraazul4=0

            if y_notabranca1>ALTURA and ponto_check_branco == 0:
                japontuoubranco_check = 0
                streak = 0
                pontos = pontos -100
                y_notabranca1=-30
                agorabranco1=0
                erros = erros + 1
            elif y_notabranca1>ALTURA and ponto_check_branco == 1:
                japontuoubranco_check = 0
                ponto_check_branco = 0
                y_notabranca1=-30
                agorabranco1=0
            if y_notabranca2>ALTURA and ponto_check_branco == 0:
                japontuoubranco_check = 0
                streak = 0
                pontos = pontos - 100
                y_notabranca2=-30
                agorabranco2=0
                erros = erros + 1
            elif y_notabranca2>ALTURA and ponto_check_branco == 1:
                japontuoubranco_check = 0
                ponto_check_branco = 0
                y_notabranca2=-30
                agorabranco2=0
            if y_notabranca3>ALTURA and ponto_check_branco == 0:
                japontuoubranco_check = 0
                streak = 0
                pontos = pontos - 1000
                y_notabranca3=-30
                agorabranco3=0
                erros = erros + 1
            elif y_notabranca3>ALTURA and ponto_check_branco == 1:
                japontuoubranco_check = 0
                ponto_check_branco = 0
                y_notabranca3=-30
                agorabranco3=0
            if y_notabranca4>ALTURA and ponto_check_branco == 0:
                japontuoubranco_check = 0
                streak = 0
                pontos = pontos-1000
                y_notabranca4=-30
                agorabranco4=0
                erros = erros + 1
            elif y_notabranca4>ALTURA and ponto_check_branco == 1:
                japontuoubranco_check = 0
                ponto_check_branco = 0
                y_notabranca4=-30
                agorabranco4=0

            for event in pygame.event.get():
                #fechar jogo
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload
                        running = False


                #Colisão de ganho de pontos
                if event.type == KEYDOWN:
                    if app_data.__controlKeyboard__ == 0:
                        if event.key == K_d and japontuouvermelho_check == 0:
                            if notavermelha1.colliderect(colisao_notavermelha) or notavermelha2.colliderect(colisao_notavermelha) or notavermelha3.colliderect(colisao_notavermelha) or notavermelha4.colliderect(colisao_notavermelha):
                                sfxSelect()
                                japontuouvermelho_check = 1
                                fill_colisao_vermelho_x= 0
                                duracao_vermelho = 30
                                ponto_check_vermelho = 1
                                if streak < 10:
                                    streak=streak+1
                                    pontos=pontos+(10*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 10  and streak <= 20:
                                    streak=streak+1
                                    pontos=pontos+(20*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 21:
                                    streak=streak+1
                                    pontos=pontos+(30*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                        elif event.key == K_f and japontuouverde_check == 0:
                            if notaverde1.colliderect(colisao_notaverde) or notaverde2.colliderect(colisao_notaverde) or notaverde3.colliderect(colisao_notaverde) or notaverde4.colliderect(colisao_notaverde):
                                sfxSelect()
                                japontuouverde_check = 1
                                fill_colisao_verde_x = 0
                                duracao_verde = 30
                                ponto_check_verde = 1
                                if streak < 10:
                                    streak=streak+1
                                    pontos=pontos+(10*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 10  and streak <= 20:
                                    streak=streak+1
                                    pontos=pontos+(20*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 21:
                                    streak=streak+1
                                    pontos=pontos+(30*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                        elif event.key == K_j  and japontuouazul_check == 0:
                            if notaazul1.colliderect(colisao_notaazul) or notaazul2.colliderect(colisao_notaazul) or notaazul3.colliderect(colisao_notaazul) or notaazul4.colliderect(colisao_notaazul):
                                sfxSelect()
                                japontuouazul_check = 1
                                fill_colisao_azul_x = 0
                                duracao_azul = 30
                                ponto_check_azul = 1
                                if streak < 10:
                                    streak=streak+1
                                    pontos=pontos+(10*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 10  and streak <= 20:
                                    streak=streak+1
                                    pontos=pontos+(20*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 21:
                                    streak=streak+1
                                    pontos=pontos+(30*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                        elif event.key == K_k  and japontuoubranco_check==0:
                            if notabranca1.colliderect(colisao_notabranca) or notabranca2.colliderect(colisao_notabranca) or notabranca3.colliderect(colisao_notabranca) or notabranca4.colliderect(colisao_notabranca):
                                sfxSelect()
                                japontuoubranco_check = 1
                                fill_colisao_branco_x = 0
                                duracao_branco = 30
                                ponto_check_branco = 1
                                if streak < 10:
                                    streak=streak+1
                                    pontos=pontos+(10*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 10 and streak <= 20:
                                    streak=streak+1
                                    pontos=pontos+(20*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 21:
                                    streak=streak+1
                                    pontos=pontos+(30*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                    else:
                        if event.key == K_LEFT and japontuouvermelho_check == 0:
                            if notavermelha1.colliderect(colisao_notavermelha) or notavermelha2.colliderect(colisao_notavermelha) or notavermelha3.colliderect(colisao_notavermelha) or notavermelha4.colliderect(colisao_notavermelha):
                                sfxSelect()
                                japontuouvermelho_check = 1
                                fill_colisao_vermelho_x= 0
                                duracao_vermelho = 30
                                ponto_check_vermelho = 1
                                if streak < 10:
                                    streak=streak+1
                                    pontos=pontos+(10*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 10  and streak <= 20:
                                    streak=streak+1
                                    pontos=pontos+(20*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 21:
                                    streak=streak+1
                                    pontos=pontos+(30*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                        elif event.key == K_DOWN and japontuouverde_check == 0:
                            if notaverde1.colliderect(colisao_notaverde) or notaverde2.colliderect(colisao_notaverde) or notaverde3.colliderect(colisao_notaverde) or notaverde4.colliderect(colisao_notaverde):
                                sfxSelect()
                                japontuouverde_check = 1
                                fill_colisao_verde_x = 0
                                duracao_verde = 30
                                ponto_check_verde = 1
                                if streak < 10:
                                    streak=streak+1
                                    pontos=pontos+(10*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 10  and streak <= 20:
                                    streak=streak+1
                                    pontos=pontos+(20*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 21:
                                    streak=streak+1
                                    pontos=pontos+(30*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                        elif event.key == K_UP  and japontuouazul_check == 0:
                            if notaazul1.colliderect(colisao_notaazul) or notaazul2.colliderect(colisao_notaazul) or notaazul3.colliderect(colisao_notaazul) or notaazul4.colliderect(colisao_notaazul):
                                sfxSelect()
                                japontuouazul_check = 1
                                fill_colisao_azul_x = 0
                                duracao_azul = 30
                                ponto_check_azul = 1
                                if streak < 10:
                                    streak=streak+1
                                    pontos=pontos+(10*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 10  and streak <= 20:
                                    streak=streak+1
                                    pontos=pontos+(20*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 21:
                                    streak=streak+1
                                    pontos=pontos+(30*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                        elif event.key == K_RIGHT  and japontuoubranco_check==0:
                            if notabranca1.colliderect(colisao_notabranca) or notabranca2.colliderect(colisao_notabranca) or notabranca3.colliderect(colisao_notabranca) or notabranca4.colliderect(colisao_notabranca):
                                sfxSelect()
                                japontuoubranco_check = 1
                                fill_colisao_branco_x = 0
                                duracao_branco = 30
                                ponto_check_branco = 1
                                if streak < 10:
                                    streak=streak+1
                                    pontos=pontos+(10*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 10 and streak <= 20:
                                    streak=streak+1
                                    pontos=pontos+(20*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak
                                elif streak >= 21:
                                    streak=streak+1
                                    pontos=pontos+(30*streak)
                                    app_data.__points__ = pontos
                                    if streak > app_data.__streak__:
                                        app_data.__streak__=streak

                #colisão de perda de pontos
                if event.type == KEYDOWN:
                    if app_data.__controlKeyboard__ == 0:
                        if event.key == K_d and ponto_check_vermelho == 0:
                            if not(notavermelha1.colliderect(colisao_notavermelha) or notavermelha2.colliderect(colisao_notavermelha) or notavermelha3.colliderect(colisao_notavermelha) or notavermelha4.colliderect(colisao_notavermelha)):
                                sfxSelect(False)
                                pontos=pontos-100
                                streak = 0
                                erros = erros + 1
                                app_data.__points__ = pontos
                                app_data.__Fail__ = erros
                        elif event.key == K_f:
                            if not(notaverde1.colliderect(colisao_notaverde) or notaverde2.colliderect(colisao_notaverde) or notaverde3.colliderect(colisao_notaverde) or notaverde4.colliderect(colisao_notaverde)):
                                sfxSelect(False)
                                pontos=pontos-100
                                streak = 0
                                erros = erros + 1
                                app_data.__points__ = pontos
                                app_data.__Fail__ = erros
                        elif event.key == K_j:
                            if not(notaazul1.colliderect(colisao_notaazul) or notaazul2.colliderect(colisao_notaazul) or notaazul3.colliderect(colisao_notaazul) or notaazul4.colliderect(colisao_notaazul)):
                                sfxSelect(False)
                                pontos=pontos-100
                                streak = 0
                                erros = erros + 1
                                app_data.__points__ = pontos
                                app_data.__Fail__ = erros
                        elif event.key == K_k:
                            if not(notabranca1.colliderect(colisao_notabranca) or notabranca2.colliderect(colisao_notabranca) or notabranca3.colliderect(colisao_notabranca) or notabranca4.colliderect(colisao_notabranca)):
                                sfxSelect(False)
                                pontos=pontos-100
                                streak = 0
                                erros = erros + 1
                                app_data.__points__ = pontos
                                app_data.__Fail__ = erros
                    else:
                        if event.key == K_LEFT and ponto_check_vermelho == 0:
                            if not(notavermelha1.colliderect(colisao_notavermelha) or notavermelha2.colliderect(colisao_notavermelha) or notavermelha3.colliderect(colisao_notavermelha) or notavermelha4.colliderect(colisao_notavermelha)):
                                sfxSelect(False)
                                pontos=pontos-100
                                streak = 0
                                erros = erros + 1
                                app_data.__points__ = pontos
                                app_data.__Fail__ = erros
                        elif event.key == K_DOWN:
                            if not(notaverde1.colliderect(colisao_notaverde) or notaverde2.colliderect(colisao_notaverde) or notaverde3.colliderect(colisao_notaverde) or notaverde4.colliderect(colisao_notaverde)):
                                sfxSelect(False)
                                pontos=pontos-100
                                streak = 0
                                erros = erros + 1
                                app_data.__points__ = pontos
                                app_data.__Fail__ = erros
                        elif event.key == K_UP:
                            if not(notaazul1.colliderect(colisao_notaazul) or notaazul2.colliderect(colisao_notaazul) or notaazul3.colliderect(colisao_notaazul) or notaazul4.colliderect(colisao_notaazul)):
                                sfxSelect(False)
                                pontos=pontos-100
                                streak = 0
                                erros = erros + 1
                                app_data.__points__ = pontos
                                app_data.__Fail__ = erros
                        elif event.key == K_RIGHT:
                            if not(notabranca1.colliderect(colisao_notabranca) or notabranca2.colliderect(colisao_notabranca) or notabranca3.colliderect(colisao_notabranca) or notabranca4.colliderect(colisao_notabranca)):
                                sfxSelect(False)
                                pontos=pontos-100
                                streak = 0
                                erros = erros + 1
                                app_data.__points__ = pontos
                                app_data.__Fail__ = erros

                #print(streak)
                drwText(pts, app_data.__setFont__(40), (255, 255, 255), tela, 625, 470)
                drwText(strk, app_data.__setFont__(20), (255, 255, 255), tela, 720, 450)
                if app_data.__streak__ >= 0 and app_data.__streak__ <= 24:
                    skin(app_data.__saveGame__-1,0,'__player0__')
                    #app_data.__setScreen__.blit(app_data.__setPlayer__(app_data.__formas__[0], '__player__'), (600, 290))
                if app_data.__streak__ >= 25 and app_data.__streak__ <= 49:
                    sfx=app_data.__streak__
                    skin(app_data.__saveGame__-1,1,'__player0__')
                if app_data.__streak__ >= 50:
                    sfx=app_data.__streak__
                    skin(app_data.__saveGame__-1,2,'__player0__')
                    #app_data.__setScreen__.blit(app_data.__setPlayer__(app_data.__formas__[2], '__player__'), (600, 290))
                pygame.display.flip()

except OSError:
    err = traceback.format_exc()
    data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    with open('Classes/Dados/Execucoes.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{data_hora} Game - OS Error:\n {err}\n\n')
        arquivo.close()
except ValueError:
    err = traceback.format_exc()
    data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    with open('Classes/Dados/Execucoes.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{data_hora} Game - Value Error:\n {err}\n\n')
        arquivo.close()
except BaseException:
    err = traceback.format_exc()
    data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    with open('Classes/Dados/Execucoes.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{data_hora} Game - Unexpected:\n {err}\n\n')
        arquivo.close()
    raise