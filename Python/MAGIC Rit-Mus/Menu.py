# -*- coding: utf-8 -*-
import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

from pygame.locals import*
from Classes import app_data
from Classes.Opcoes import call_Options, drwText, effectPlay, effectBack, btnBack
from Classes.app_data import __setCursor__, __saveConfig__, __callRanking__, __formas__, sfxSelect, __saveRanking__
from Classes.Game import call_game
from Classes.Creditos import call_credits
from pygame import mixer
import pygame as pg, traceback
from datetime import datetime

try:

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()

    screen = app_data.__setScreen__
    app_data.__setTitle__
    app_data.__setIcon__

    btnsAzul = ['Imagens/Botões/jogar_1.png', 'Imagens/Botões/galeria_1.png',
                'Imagens/Botões/opcoes_2.png', 'Imagens/Botões/creditos_2.png']

    btnsStar = ['Imagens/BG/Star0.png', 'Imagens/BG/Star1.png',
                'Imagens/BG/Star2.png','Imagens/BG/Star3.png',
                'Imagens/BG/Stars.png']

    playAzul = pg.image.load(btnsAzul[0])
    Galeria = pg.image.load(btnsAzul[1])
    OpcAzul = pg.image.load(btnsAzul[2])
    CredAzul = pg.image.load(btnsAzul[3])
    btnPlay = pg.draw.rect(app_data.__setScreen__, (0, 0, 0), pg.Rect(580, 475, 120, 42))

    Star0 = pg.image.load(btnsStar[0])
    Star1 = pg.image.load(btnsStar[1])
    Star2 = pg.image.load(btnsStar[2])
    Star3 = pg.image.load(btnsStar[3])
    Stars = pg.image.load(btnsStar[4])

    btnJogar = pg.Rect((app_data.__largura__ / 2 - 264 / 2), 260, 264, 70)
    btnGaleria = pg.Rect((app_data.__largura__ / 2 - 264 / 2), 340, 264, 70)
    btnOpcoes = pg.Rect((app_data.__largura__ / 2 - 264 / 2), 420, 264, 70)
    btnCreditos = pg.Rect((app_data.__largura__ / 2 - 264 / 2), 500, 264, 70)

    btnCircle = pg.draw.rect(app_data.__setScreen__, (0, 0, 255), pg.Rect(410, 320, 120, 120))
    btnTriangle = pg.draw.rect(app_data.__setScreen__, (255, 0, 0), pg.Rect(580, 320, 120, 120))
    btnSquare = pg.draw.rect(app_data.__setScreen__, (252, 204, 0), pg.Rect(750, 320, 120, 120))

    def call_pre():
        def skin(forma,skin,level):
            app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[forma], level, skin), (410, 320))

        def drwScreen(save=0, selected=0, play=False):
            if save == 0 and play == False:
                app_data.__setScreen__.fill((0, 0, 0))
                app_data.__setScreen__.blit(app_data.__bgVerde__, (0, 0))
                app_data.__setScreen__.blit(app_data.__logoGame__, ((1280 / 2 - app_data.__logoGame__.
                                                                     get_width() / 2), 50))

                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[0], '__player__'), (410, 320))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[1], '__player__', 0, 140), (565, 320))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[2], '__player__'), (750, 320))
            elif save == 1 and play == False:
                app_data.__setScreen__.fill((0, 0, 0))
                app_data.__setScreen__.blit(app_data.__bgVerde__, (0, 0))
                app_data.__setScreen__.blit(app_data.__logoGame__, ((1280 / 2 - app_data.__logoGame__.
                                                                     get_width() / 2), 50))

                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[0], '__player__'), (410, 320))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[1], '__player__', 0, 140), (565, 320))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[2], '__player__'), (750, 320))

                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[0], '__player0__', 1), (120, 145))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[0], '__player1__', 4), (120, 520))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[0], '__player2__', 7), (1040, 120))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[0], '__player3__', 11), (1040, 520))

                drwText('Jogar', app_data.__setFont__(36), (255, 255, 255), app_data.__setScreen__, 582, 460)
                pg.draw.rect(app_data.__setScreen__, (255, 255, 255), pg.Rect(410, 320, 120, 120), 4)
            elif save == 2 and play == False:
                app_data.__setScreen__.fill((0, 0, 0))
                app_data.__setScreen__.blit(app_data.__bgVerde__, (0, 0))
                app_data.__setScreen__.blit(app_data.__logoGame__, ((1280 / 2 - app_data.__logoGame__.
                                                                     get_width() / 2), 50))

                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[0], '__player__'), (410, 320))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[1], '__player__', 0, 140), (565, 320))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[2], '__player__'), (750, 320))

                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[1], '__player0__', 2), (120, 145))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[1], '__player1__', 5), (120, 520))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[1], '__player2__', 7), (1040, 120))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[1], '__player3__', 11), (1040, 520))

                drwText('Jogar', app_data.__setFont__(36), (255, 255, 255), app_data.__setScreen__, 582, 460)
                pg.draw.rect(app_data.__setScreen__, (255, 255, 255), pg.Rect(565, 320, 140, 120), 4)
            elif save == 3 and play == False:
                app_data.__setScreen__.fill((0, 0, 0))
                app_data.__setScreen__.blit(app_data.__bgVerde__, (0, 0))
                app_data.__setScreen__.blit(app_data.__logoGame__, ((1280 / 2 - app_data.__logoGame__.
                                                                     get_width() / 2), 50))

                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[0], '__player__'), (410, 320))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[1], '__player__', 0, 140), (565, 320))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[2], '__player__'), (750, 320))

                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[2], '__player0__', 1), (120, 145))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[2], '__player1__', 4), (120, 520))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[2], '__player2__', 6), (1040, 120))
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[2], '__player3__', 10), (1040, 520))

                drwText('Jogar', app_data.__setFont__(36), (255, 255, 255), app_data.__setScreen__, 582, 460)
                pg.draw.rect(app_data.__setScreen__, (255, 255, 255), pg.Rect(750, 320, 120, 120), 4)
        __optionSelected__ = 0

        try:
            pg.init()
            app_data.__setTitle__
            app_data.__setIcon__

            running = True
            play = False
            OnP = False
            OnB = False
            while running:
                app_data.__points__ = 0000
                app_data.__streak__ = 0
                app_data.__Fail__ = 0
                drwScreen(app_data.__saveGame__, __optionSelected__, play)
                coord = pg.mouse.get_pos()
                effectPlay(OnP)
                effectBack(OnB)
                __setCursor__(coord)
                for event in pg.event.get():
                    if event.type == QUIT:
                        __saveConfig__()
                        pg.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            app_data.__situacao__ = 'off'
                            running = False
                    if btnCircle.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                __optionSelected__ = 1
                                __saveGame__ = __optionSelected__
                                app_data.__saveGame__ = __saveGame__
                                sfxSelect()
                    if btnTriangle.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                __optionSelected__ = 2
                                __saveGame__ = __optionSelected__
                                app_data.__saveGame__ = __saveGame__
                                sfxSelect()
                    if btnSquare.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                __optionSelected__ = 3
                                __saveGame__ = __optionSelected__
                                app_data.__saveGame__ = __saveGame__
                                sfxSelect()
                    if btnPlay.collidepoint(coord):
                        OnP = True
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                mixer.music.stop()
                                mixer.music.unload
                                app_data.__situacao__ = 'pos'
                                call_game()
                                running = False
                    else:
                        OnP = False
                    if btnBack.collidepoint(coord):
                        OnB = True
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                app_data.__situacao__ = 'off'
                                running = False
                    else:
                        OnB = False

                pg.display.flip()
                app_data.__setMainClock__.tick(60)
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
    def call_pos():
        def skinPos(forma, skin, level):
            if skin!=2:
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[forma], level, skin), (600, 250))
            else:
                app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[forma], level, skin), (600, 200))

            Stars = pg.image.load('Imagens/BG/Stars.png')
            Stars = pg.transform.scale(Stars, (230,100))
            if forma == 0:
                app_data.__setScreen__.blit(Stars, (540, 360))
            elif forma == 1:
                app_data.__setScreen__.blit(Stars, (540, 360))
            elif forma == 2:
                app_data.__setScreen__.blit(Stars, (540, 360))
        def drwScreen2(save=0, selected=0, play=False):
            app_data.__setScreen__.fill((0, 0, 0))
            app_data.__setScreen__.blit(app_data.__bgGame__, (0, 0))
            app_data.__setScreen__.blit(app_data.__logoGame__, ((1280 / 2 - app_data.__logoGame__.
                                                                 get_width() / 2), 50))

        def effectPlay2(On=False):
            if On != True:
                effect = drwText('Continuar', app_data.__setFont__(36), (255, 255, 255), app_data.__setScreen__, 576,470)
                return effect
            else:
                effect = drwText('Continuar', app_data.__setFont__(36), (255, 200, 0), app_data.__setScreen__, 576, 470)
                return effect

        __optionSelected__ = 0
        try:
            pg.init()
            app_data.__setTitle__
            app_data.__setIcon__
            mixer.music.load("Sounds/Self_esteem.wav")
            mixer.music.set_volume(app_data.__setVolume__)  # valor entre 0.0 e 1.0
            mixer.music.play(-1)
            running = True
            play = False
            On = False
            while running:
                drwScreen2(app_data.__saveGame__, __optionSelected__, play)
                coord = pg.mouse.get_pos()
                effectPlay2(On)
                if app_data.__streak__ >= 0 and app_data.__streak__ <= 24:
                    skinPos(app_data.__saveGame__ - 1, 0, '__player0__')
                if app_data.__streak__ >= 25 and app_data.__streak__ <= 49:
                    skinPos(app_data.__saveGame__ - 1, 1, '__player0__')
                if app_data.__streak__ >= 50:
                    skinPos(app_data.__saveGame__ - 1, 2, '__player0__')
                drwText(f'DESEMPENHO', app_data.__setFont__(40), (255, 255, 255), app_data.__setScreen__, 160, 151)
                drwText(f'DESEMPENHO', app_data.__setFont__(40), (255, 46, 0), app_data.__setScreen__, 162, 152)
                drwText(f'Pontos  {app_data.__points__}', app_data.__setFont__(30), (255, 255, 255), app_data.__setScreen__, 100, 250)
                drwText(f'Combo  {app_data.__streak__}', app_data.__setFont__(30), (255, 255, 255), app_data.__setScreen__, 100, 300)
                drwText(f'Erros  {app_data.__Fail__}', app_data.__setFont__(30), (255, 255, 255), app_data.__setScreen__, 100, 350)
                drwText('SKINS', app_data.__setFont__(26), (3, 248, 57), app_data.__setScreen__, 250, 450)
                setStar = 0
                if app_data.__streak__ <= 19:
                    if __formas__[app_data.__saveGame__-1]=='Circle':
                        app_data.__skinCircleOpen__=setStar
                        app_data.lstConfig[9]=setStar
                    if __formas__[app_data.__saveGame__-1]=='Triangle':
                        app_data.__skinTriangleOpen__=setStar
                        app_data.lstConfig[10]=setStar
                    if __formas__[app_data.__saveGame__-1]=='Square':
                        app_data.__skinSquareOpen__=setStar
                        app_data.lstConfig[11]=setStar
                    app_data.__setScreen__.blit(app_data.__setPlayer__
                                                (__formas__[app_data.__saveGame__-1], '__player0__', 0), (100, 550))
                if app_data.__streak__ >= 20 and app_data.__streak__ <= 49:
                    if __formas__[app_data.__saveGame__-1]=='Circle':
                        app_data.__skinCircleOpen__=setStar+1
                        app_data.lstConfig[9]=setStar+1
                    if __formas__[app_data.__saveGame__-1]=='Triangle':
                        app_data.__skinTriangleOpen__=setStar+1
                        app_data.lstConfig[10]=setStar+1
                    if __formas__[app_data.__saveGame__-1]=='Square':
                        app_data.__skinSquareOpen__=setStar+1
                        app_data.lstConfig[11]=setStar+1
                    app_data.__setScreen__.blit(app_data.__setPlayer__
                                                (__formas__[app_data.__saveGame__-1], '__player0__', 0), (100, 550))
                    app_data.__setScreen__.blit(app_data.__setPlayer__
                                                (__formas__[app_data.__saveGame__-1], '__player0__', 1), (250, 550))
                if app_data.__streak__ >= 50:
                    if __formas__[app_data.__saveGame__-1]=='Circle':
                        app_data.__skinCircleOpen__=setStar+2
                        app_data.lstConfig[9]=setStar+2
                    if __formas__[app_data.__saveGame__-1]=='Triangle':
                        app_data.__skinTriangleOpen__=setStar+2
                        app_data.lstConfig[10]=setStar+2
                    if __formas__[app_data.__saveGame__-1]=='Square':
                        app_data.__skinSquareOpen__=setStar+2
                        app_data.lstConfig[11]=setStar+2
                    app_data.__setScreen__.blit(app_data.__setPlayer__
                                                (__formas__[app_data.__saveGame__-1], '__player0__', 0), (100, 550))
                    app_data.__setScreen__.blit(app_data.__setPlayer__
                                                (__formas__[app_data.__saveGame__-1], '__player0__', 1), (250, 550))
                    app_data.__setScreen__.blit(app_data.__setPlayer__
                                                (__formas__[app_data.__saveGame__-1], '__player0__', 2), (400, 500))
                __setCursor__(coord)

                for event in pg.event.get():
                    if event.type == QUIT:
                        __saveConfig__()
                        __saveRanking__()
                        app_data.__situacao__='off'
                        running = False
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            __saveConfig__()
                            __saveRanking__()
                            app_data.__situacao__='off'
                            running = False
                    if btnPlay.collidepoint(coord):
                        On = True
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                __saveRanking__()
                                app_data.__situacao__='off'
                                running = False
                    else:
                        On = False

                pg.display.flip()
                app_data.__setMainClock__.tick(60)
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
    def call_galeria():
        def drwScreen2(save=0, selected=0, play=False, next=0):
            app_data.__setScreen__.fill((0, 0, 0))
            if next==0:
                app_data.__setScreen__.blit(app_data.__bgGalCircle__, (0, 0))
            elif next==1:
                app_data.__setScreen__.blit(app_data.__bgGalTriangle__, (0, 0))
            elif next==2:
                app_data.__setScreen__.blit(app_data.__bgGalSquare__, (0, 0))

            if next==0:
                if app_data.__skinCircleOpen__==0:
                    app_data.__setScreen__.blit(Star1, (275, 368))
                    app_data.__setScreen__.blit(Star0, (300, 598))
                    app_data.__setScreen__.blit(Star0, (720, 368))
                    app_data.__setScreen__.blit(Star0, (720, 598))
                if app_data.__skinCircleOpen__==1:
                    app_data.__setScreen__.blit(Star2, (275, 368))
                    app_data.__setScreen__.blit(Star0, (300, 598))
                    app_data.__setScreen__.blit(Star0, (720, 368))
                    app_data.__setScreen__.blit(Star0, (720, 598))
                if app_data.__skinCircleOpen__==2:
                    app_data.__setScreen__.blit(Star3, (275, 368))
                    app_data.__setScreen__.blit(Star0, (300, 598))
                    app_data.__setScreen__.blit(Star0, (720, 368))
                    app_data.__setScreen__.blit(Star0, (720, 598))
            elif next == 1:
                if app_data.__skinTriangleOpen__ == 0:
                    app_data.__setScreen__.blit(Star1, (275, 368))
                    app_data.__setScreen__.blit(Star0, (300, 598))
                    app_data.__setScreen__.blit(Star0, (720, 368))
                    app_data.__setScreen__.blit(Star0, (720, 598))
                if app_data.__skinTriangleOpen__ == 1:
                    app_data.__setScreen__.blit(Star2, (275, 368))
                    app_data.__setScreen__.blit(Star0, (300, 598))
                    app_data.__setScreen__.blit(Star0, (720, 368))
                    app_data.__setScreen__.blit(Star0, (720, 598))
                if app_data.__skinTriangleOpen__ == 2:
                    app_data.__setScreen__.blit(Star3, (275, 368))
                    app_data.__setScreen__.blit(Star0, (300, 598))
                    app_data.__setScreen__.blit(Star0, (720, 368))
                    app_data.__setScreen__.blit(Star0, (720, 598))
            elif next == 2:
                if app_data.__skinSquareOpen__ == 0:
                    app_data.__setScreen__.blit(Star1, (275, 368))
                    app_data.__setScreen__.blit(Star0, (300, 598))
                    app_data.__setScreen__.blit(Star0, (720, 368))
                    app_data.__setScreen__.blit(Star0, (720, 598))
                if app_data.__skinSquareOpen__ == 1:
                    app_data.__setScreen__.blit(Star2, (275, 368))
                    app_data.__setScreen__.blit(Star0, (300, 598))
                    app_data.__setScreen__.blit(Star0, (720, 368))
                    app_data.__setScreen__.blit(Star0, (720, 598))
                if app_data.__skinSquareOpen__ == 2:
                    app_data.__setScreen__.blit(Star3, (275, 368))
                    app_data.__setScreen__.blit(Star0, (300, 598))
                    app_data.__setScreen__.blit(Star0, (720, 368))
                    app_data.__setScreen__.blit(Star0, (720, 598))

            app_data.__setScreen__.blit(app_data.__logoGame__, ((app_data.__largura__ / 2 - app_data.__logo__.
                                                                get_width() / 2), 50))

        __optionSelected__ = 0

        btnLeft = pg.Rect(160, 400, 80, 60)
        btnRight = pg.Rect(1040, 400, 80, 60)

        try:
            pg.init()
            app_data.__setTitle__
            app_data.__setIcon__
            running = True
            play = False
            OnB = False
            next = 0
            while running:
                drwScreen2(app_data.__saveGame__, __optionSelected__, play, next)
                coord = pg.mouse.get_pos()
                effectBack(OnB)
                __setCursor__(coord)
                for event in pg.event.get():
                    if event.type == QUIT:
                        __saveConfig__()
                        pg.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            __saveConfig__()
                            running = False
                    if btnBack.collidepoint(coord):
                        OnB = True
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                running = False
                    else:
                        OnB = False
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if btnLeft.collidepoint(coord):
                                sfxSelect()
                                if next==0:
                                    next=2
                                elif next==1:
                                    next=0
                                elif next==2:
                                    next=1
                            if btnRight.collidepoint(coord):
                                sfxSelect()
                                if next==0:
                                    next=1
                                elif next==1:
                                    next=2
                                elif next==2:
                                    next=0


                pg.display.flip()
                app_data.__setMainClock__.tick(60)
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

    def drwLOGO():
        screen.fill((0, 0, 0))
        pg.draw.rect(screen, (0, 200, 255), btnJogar, 1)
        pg.draw.rect(screen, (0, 200, 255), btnOpcoes, 1)
        pg.draw.rect(screen, (0, 200, 255), btnCreditos, 1)
        screen.blit(app_data.__bgRoxo__, (0, 0))
        screen.blit(app_data.__logoGame__, ((app_data.__largura__ / 2 - app_data.__logo__.
                                                                get_width() / 2), 50))
    def drwAzul(botao=0):

            screen.blit(playAzul, ((app_data.__largura__ / 2 - playAzul.get_width() / 2), 260))
            screen.blit(Galeria, ((app_data.__largura__ / 2 - Galeria.get_width() / 2), 340))
            screen.blit(OpcAzul, ((app_data.__largura__ / 2 - OpcAzul.get_width() / 2), 420))
            screen.blit(CredAzul, ((app_data.__largura__ / 2 - CredAzul.get_width() / 2), 500))
            drwRanking()
    click = False
    def mainMenu():
        counter, text = 10, '10'.rjust(3)
        pg.time.set_timer(pg.USEREVENT, 1000)
        # Sound
        mixer.music.load("Sounds/Self_esteem.wav")
        mixer.music.set_volume(app_data.__setVolume__)  # valor entre 0.0 e 1.0
        mixer.music.play(-1)  # valor -1 permanece em loop infinito
        BOTAO = 0 #variavel que define qual botão está selecionado

        while True:  # LOOP PRINIPAL

                app_data.__setTitle__
                app_data.__setIcon__
                coord = pg.mouse.get_pos()
                if counter % 2 == 0:
                    drwLOGO()
                    drwAzul(0)
                    drwAzul(1)
                    drwAzul(2)
                    __setCursor__(coord)
                    if BOTAO == 0:
                        drwAzul(1)
                        __setCursor__(coord)

                    elif BOTAO == 1:
                        drwAzul(0)
                        __setCursor__(coord)

                    elif BOTAO == 2:
                        drwAzul(0)
                        __setCursor__(coord)

                    if app_data.__situacao__=='pre':
                        call_pre()
                    elif app_data.__situacao__=='pos':
                        call_pos()

                    for event in pg.event.get():
                        if event.type == QUIT:
                            pg.quit()
                            sys.exit()
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                if btnJogar.collidepoint(coord):
                                    sfxSelect()
                                    app_data.__situacao__='pre'
                                if btnOpcoes.collidepoint(coord):
                                    sfxSelect()
                                    call_Options()
                                if btnCreditos.collidepoint(coord):
                                    sfxSelect()
                                    call_credits()
                                if btnGaleria.collidepoint(coord):
                                    sfxSelect()
                                    call_galeria()
                    pg.display.flip()
                    app_data.__setMainClock__.tick(60)

                pg.display.flip()
                app_data.__setMainClock__.tick(60)
    def drwRanking():
        def ranking():
            drwText('Personagem', app_data.__setFont__(20), (255, 255, 255), screen, 40, 200)
            drwText('Pontos', app_data.__setFont__(20), (255, 255, 255), screen, 190, 200)
            drwText('Combo', app_data.__setFont__(20), (255, 255, 255), screen, 300, 200)

            app_data.__setScreen__.blit(
                    app_data.__setPlayer__(__callRanking__(0, '__Player__'), '__player__', 0, 50, 45), (70, 245))
            app_data.__setScreen__.blit(
                    app_data.__setPlayer__(__callRanking__(1, '__Player__'), '__player__', 0, 50, 45), (70, 300))
            app_data.__setScreen__.blit(
                    app_data.__setPlayer__(__callRanking__(2, '__Player__'), '__player__', 0, 50, 45), (70, 360))
            app_data.__setScreen__.blit(
                    app_data.__setPlayer__(__callRanking__(3, '__Player__'), '__player__', 0, 50, 45), (70, 420))
            app_data.__setScreen__.blit(
                    app_data.__setPlayer__(__callRanking__(4, '__Player__'), '__player__', 0, 50, 45), (70, 480))

            drwText(__callRanking__(0,'__Points__'), app_data.__setFont__(20), (255, 255, 255), screen, 190, 250)
            drwText(__callRanking__(0,'__Streak__'), app_data.__setFont__(20), (255, 255, 255), screen, 300, 250)

            drwText(__callRanking__(1,'__Points__'), app_data.__setFont__(20), (255, 255, 255), screen, 190, 310)
            drwText(__callRanking__(1,'__Streak__'), app_data.__setFont__(20), (255, 255, 255), screen, 300, 310)

            drwText(__callRanking__(2,'__Points__'), app_data.__setFont__(20), (255, 255, 255), screen, 190, 370)
            drwText(__callRanking__(2,'__Streak__'), app_data.__setFont__(20), (255, 255, 255), screen, 300, 370)

            drwText(__callRanking__(3,'__Points__'), app_data.__setFont__(20), (255, 255, 255), screen, 190, 430)
            drwText(__callRanking__(3,'__Streak__'), app_data.__setFont__(20), (255, 255, 255), screen, 300, 430)

            drwText(__callRanking__(4,'__Points__'), app_data.__setFont__(20), (255, 255, 255), screen, 190, 490)
            drwText(__callRanking__(4,'__Streak__'), app_data.__setFont__(20), (255, 255, 255), screen, 300, 490)

        drwText('RANKING', app_data.__setFont__(36), (255, 255, 255), screen, 100, 130)
        ranking()

    mainMenu()

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