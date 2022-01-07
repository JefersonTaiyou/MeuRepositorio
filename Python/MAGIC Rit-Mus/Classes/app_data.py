# -*- coding: utf-8 -*-
import pygame as pg
import os, traceback
from datetime import datetime

#largura altura titulo volMax volMin volMusic, volSFX keyDefault saveGame lvlCircle lvlTriangle lvlSquare
lstConfigDefault = [1280,700,'MAGIC Rit-Mus',1.0,0.1,0.2,0.6,0,0,0,0,0]
lstRanking = []
lstConfig = []

with open('Classes/Dados/Config.dat', 'r') as arquivo:
    arq_leitura = open('Classes/Dados/Config.dat', 'r', encoding='utf-8')
    for paragrafo in arq_leitura:
        paragrafo = paragrafo.replace('\n', '')
        lstConfig.append(paragrafo)
    arq_leitura.close()
arquivo.close()


dicionario ={"Rank1":"","Rank2":"",
             "Rank3":"", "Rank4":"",
             "Rank5":""}

__situacao__ = 'off'
__controlKeyboard__ = int(lstConfig[7]) #0 - Padrão(DFJK) / 1 - Setas(Direção)
__setMainClock__ = pg.time.Clock()
__largura__, __altura__ = int(lstConfig[0]), int(lstConfig[1])
__setResolution__ = (__largura__, __altura__)
__setScreen__ = pg.display.set_mode((__setResolution__))
__saveGame__ = int(lstConfig[8])
__formas__ = ['Circle','Triangle','Square']
__skinCheckBola__ = 0
__skinCheckTriangulo__ = 0
__skinCheckQuadrado__ = 0

__player__ = 'Circle'
__points__ = 0000
__streak__ = 0
__Fail__ = 0

__skinCircleOpen__ = int(lstConfig[9])
__skinTriangleOpen__ = int(lstConfig[10])
__skinSquareOpen__ = int(lstConfig[11])

__pathBackground__ = ['bgLaranjaMenu.png', 'bgRoxoMenu.png', 'bgVerdeMenu.png']
__pathGaleria__ = ['gaCircle.png','gaTriangle.png','gaSquare.png']

__bgLaranja__ = pg.image.load(f'Imagens/Formas/{__pathBackground__[0]}')
__bgLaranja__ = pg.transform.scale(__bgLaranja__, (__setResolution__))
__bgRoxo__ = pg.image.load(f'Imagens/Formas/{__pathBackground__[1]}')
__bgRoxo__ = pg.transform.scale(__bgRoxo__, (__setResolution__))
__bgVerde__ = pg.image.load(f'Imagens/Formas/{__pathBackground__[2]}')
__bgVerde__ = pg.transform.scale(__bgVerde__, (__setResolution__))

__bgGame__ = pg.image.load('Imagens/BG/Ativo168.png')
__bgGame__ = pg.transform.scale(__bgGame__, (__setResolution__))

__bgGalCircle__ = pg.image.load(f'Imagens/BG/{__pathGaleria__[0]}')
__bgGalCircle__ = pg.transform.scale(__bgGalCircle__, (__setResolution__))
__bgGalTriangle__ = pg.image.load(f'Imagens/BG/{__pathGaleria__[1]}')
__bgGalTriangle__ = pg.transform.scale(__bgGalTriangle__, (__setResolution__))
__bgGalSquare__ = pg.image.load(f'Imagens/BG/{__pathGaleria__[2]}')
__bgGalSquare__ = pg.transform.scale(__bgGalSquare__, (__setResolution__))

__pathLogo__ = ['LogoMagus.png', 'LogoRitmus.png', 'Icone.png','mouse45_1.png']

__pathPlayerCircle__ = ['1-1padrao.png','1-2padrao.png','1-3padrao.png',
                        '2-1padrao.png','2-2padrao.png','4-3padrao.png',
                        '3-1padrao.png','3-2padrao.png','4-3padrao.png',
                        '4-1padrao.png','4-2padrao.png','4-3padrao.png']
__pathPlayerTriangle__ = ['1-1padrao.png','1-2padrao.png','1-3padrao.png',
                        '2-1padrao.png','2-2padrao.png','4-3padrao.png',
                        '3-1padrao.png','3-2padrao.png','4-3padrao.png',
                        '4-1padrao.png','4-2padrao.png','4-3padrao.png']
__pathPlayerSquare__ = ['1-1padrao.png','1-2padrao.png','1-3padrao.png',
                        '2-1padrao.png','2-2padrao.png','4-3padrao.png',
                        '3-1padrao.png','3-2padrao.png','4-3padrao.png',
                        '4-1padrao.png','4-2padrao.png','4-3padrao.png']

__logo__ = pg.image.load(f'Imagens/Botões/{__pathLogo__[0]}')
__logo__ = pg.transform.scale(__logo__, (264, 160))

__logoGame__ = pg.image.load(f'Imagens/1x/{__pathLogo__[1]}')
__logoGame__ = pg.transform.scale(__logoGame__, (264, 160))

__icon__ = pg.image.load(f'Imagens/1x/{__pathLogo__[2]}')
__cursor__ = pg.image.load(f'Imagens/1x/{__pathLogo__[3]}')
__setIcon__ = pg.display.set_icon(__icon__)
__title__ = lstConfig[2]
__setTitle__ = pg.display.set_caption(__title__)

__volumeMax__, __volumeMin__, __setVolume__, __setSFX__ = float(lstConfig[3]), float(lstConfig[4]), float(lstConfig[5]), float(lstConfig[6])

def __setPlayer__(forma='Circle', player='__player__',skin=0, largura=120,altura=120):

    if forma == 'Circle':
        if player=='__player__': # 0 1 2
            __player__ = pg.image.load(f'Imagens/1x/Circle/{__pathPlayerCircle__[skin]}')
            __player__ = pg.transform.scale(__player__, (largura, altura))
            return __player__
        elif player=='__player0__': # 0 1 2
            __player0__ = pg.image.load(f'Imagens/1x/Circle/{__pathPlayerCircle__[skin]}')
            __player0__ = pg.transform.scale(__player0__, (int(__player0__.get_width() / 2)+20, int(__player0__.get_height() / 2)+20))
            return __player0__
        if player=='__player1__': # 3 4 5
            __player1__ = pg.image.load(f'Imagens/1x/Circle/{__pathPlayerCircle__[skin]}')
            __player1__ = pg.transform.scale(__player1__, (int(__player1__.get_width() / 2), int(__player1__.get_height() / 2)))
            return __player1__
        if player=='__player2__': # 6 7 8
            __player2__ = pg.image.load(f'Imagens/1x/Circle/{__pathPlayerCircle__[skin]}')
            __player2__ = pg.transform.scale(__player2__, (int(__player2__.get_width() / 2), int(__player2__.get_height() / 2)))
            return __player2__
        if player=='__player3__': # 9 10 11
            __player3__ = pg.image.load(f'Imagens/1x/Circle/{__pathPlayerCircle__[skin]}')
            __player3__ = pg.transform.scale(__player3__, (int(__player3__.get_width() / 2), int(__player3__.get_height() / 2)))
            return __player3__
    elif forma=='Triangle':
        if player=='__player__':
            __player__ = pg.image.load(f'Imagens/1x/Triangle/{__pathPlayerTriangle__[skin]}')
            __player__ = pg.transform.scale(__player__, (largura, altura))
            return __player__
        elif player=='__player0__':
            __player0__ = pg.image.load(f'Imagens/1x/Triangle/{__pathPlayerTriangle__[skin]}')
            __player0__ = pg.transform.scale(__player0__, (int(__player0__.get_width() / 2)+20, int(__player0__.get_height() / 2)+20))
            return __player0__
        if player=='__player1__':
            __player1__ = pg.image.load(f'Imagens/1x/Triangle/{__pathPlayerTriangle__[skin]}')
            __player1__ = pg.transform.scale(__player1__, (int(__player1__.get_width() / 2), int(__player1__.get_height() / 2)))
            return __player1__
        if player=='__player2__':
            __player2__ = pg.image.load(f'Imagens/1x/Triangle/{__pathPlayerTriangle__[skin]}')
            __player2__ = pg.transform.scale(__player2__, (int(__player2__.get_width() / 2), int(__player2__.get_height() / 2)))
            return __player2__
        if player=='__player3__':
            __player3__ = pg.image.load(f'Imagens/1x/Triangle/{__pathPlayerTriangle__[skin]}')
            __player3__ = pg.transform.scale(__player3__, (int(__player3__.get_width() / 2), int(__player3__.get_height() / 2)))
            return __player3__
    elif forma=='Square':
        if player=='__player__':
            __player__ = pg.image.load(f'Imagens/1x/Square/{__pathPlayerSquare__[skin]}')
            __player__ = pg.transform.scale(__player__, (largura, altura))
            return __player__
        elif player=='__player0__':
            __player0__ = pg.image.load(f'Imagens/1x/Square/{__pathPlayerSquare__[skin]}')
            __player0__ = pg.transform.scale(__player0__, (int(__player0__.get_width() / 2)+20, int(__player0__.get_height() / 2)+20))
            return __player0__
        if player=='__player1__':
            __player1__ = pg.image.load(f'Imagens/1x/Square/{__pathPlayerSquare__[skin]}')
            __player1__ = pg.transform.scale(__player1__, (int(__player1__.get_width() / 2), int(__player1__.get_height() / 2)))
            return __player1__
        if player=='__player2__':
            __player2__ = pg.image.load(f'Imagens/1x/Square/{__pathPlayerSquare__[skin]}')
            __player2__ = pg.transform.scale(__player2__, (int(__player2__.get_width() / 2), int(__player2__.get_height() / 2)))
            return __player2__
        if player=='__player3__':
            __player3__ = pg.image.load(f'Imagens/1x/Square/{__pathPlayerSquare__[skin]}')
            __player3__ = pg.transform.scale(__player3__, (int(__player3__.get_width() / 2), int(__player3__.get_height() / 2)))
            return __player3__

def __setCursor__(coord=0):
    cursor = __cursor__
    cursor = pg.transform.scale(cursor, (40, 40))
    pg.mouse.set_visible(False)
    __setScreen__.blit(cursor, coord)
def __setFont__(tam=24):
    font = pg.font.Font("fonts/NaishilaDancingScript.ttf", tam)
    return font
def __saveConfig__():
    try:
        with open('Classes/Dados/Config.dat', 'w') as arquivo:
            arq_escrita = open('Classes/Dados/Config.dat', 'w', encoding='utf-8')
            arq_escrita.write(f'{__largura__}\n')
            arq_escrita.write(f'{__altura__}\n')
            arq_escrita.write(f'{__title__}\n')
            arq_escrita.write(f'{__volumeMax__}\n')
            arq_escrita.write(f'{__volumeMin__}\n')
            arq_escrita.write(f'{__setVolume__}\n')
            arq_escrita.write(f'{__setSFX__}\n')
            arq_escrita.write(f'{__controlKeyboard__}\n')
            arq_escrita.write(f'{__saveGame__}\n')
            arq_escrita.write(f'{__skinCircleOpen__}\n')
            arq_escrita.write(f'{__skinTriangleOpen__}\n')
            arq_escrita.write(f'{__skinSquareOpen__}\n')
            arq_escrita.close()
        arquivo.close()
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
        with open('Dados/Execucoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{data_hora} Game - Unexpected:\n {err}\n\n')
            arquivo.close()
        raise
def __saveRanking__():
    try:
        with open('Classes/Dados/Ranking.dat', 'a') as arquivo:
            arq_escrita = open('Classes/Dados/Ranking.dat', 'a', encoding='utf-8')
            arq_escrita.write(f'\n{__player__} {__points__} {__streak__}')
            arq_escrita.close()
        arquivo.close()
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


def sfxSelect(atv=True):
    # check-off 4-Click
    if atv != True:
        sfx = pg.mixer.Sound("Sounds/check-off.wav")
        sfx.set_volume(__setSFX__)  # valor entre 0.0 e 1.0
        sfx.play()
    else:
        sfx = pg.mixer.Sound("Sounds/4-Click.wav")
        sfx.set_volume(__setSFX__)  # valor entre 0.0 e 1.0
        sfx.play()
def __callRanking__(pos=0,info='info'):
    rank = [linha.replace('\n', '') for linha in open('Classes/Dados/Ranking.dat', 'r', encoding='utf-8')]
    rank = [linha.split() for linha in rank]
    order = sorted([[x, int(y), int(z)] for x, y, z in rank], key=lambda item: item[1], reverse=True)

    for alt in range(len(dicionario)):
        key = f'Rank{alt + 1}'
        dicionario[key] = order[alt]

    if info=='__Player__':
        if pos==0:
            __rnkPlayer__ = order[pos][0]
            return __rnkPlayer__
        elif pos==1:
            __rnkPlayer__ = order[pos][0]
            return str(__rnkPlayer__)
        elif pos==2:
            __rnkPlayer__ = order[pos][0]
            return __rnkPlayer__
        elif pos==3:
            __rnkPlayer__ = order[pos][0]
            return __rnkPlayer__
        elif pos==4:
            __rnkPlayer__ = order[pos][0]
            return __rnkPlayer__
    if info=='__Points__':
        if pos==0:
            __rnkPoints__ = order[pos][1]
            return str(__rnkPoints__)
        elif pos==1:
            __rnkPoints__ = order[pos][1]
            return str(__rnkPoints__)
        elif pos==2:
            __rnkPoints__ = order[pos][1]
            return str(__rnkPoints__)
        elif pos==3:
            __rnkPoints__ = order[pos][1]
            return str(__rnkPoints__)
        elif pos==4:
            __rnkPoints__ = order[pos][1]
            return str(__rnkPoints__)
    if info=='__Streak__':
        if pos==0:
            __rnkStreak__ = order[pos][2]
            return str(__rnkStreak__)
        elif pos==1:
            __rnkStreak__ = order[pos][2]
            return str(__rnkStreak__)
        elif pos==2:
            __rnkStreak__ = order[pos][2]
            return str(__rnkStreak__)
        elif pos==3:
            __rnkStreak__ = order[pos][2]
            return str(__rnkStreak__)
        elif pos==4:
            __rnkStreak__ = order[pos][2]
            return str(__rnkStreak__)


