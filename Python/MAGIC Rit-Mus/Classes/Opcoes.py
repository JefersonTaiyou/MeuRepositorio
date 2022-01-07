# -*- coding: utf-8 -*-
from datetime import datetime
from pygame import mixer
import traceback, pygame as pg, sys, os
from pygame.locals import*
from Classes import app_data
from Classes.app_data import __setCursor__, __setFont__, __setVolume__, __saveConfig__, __formas__, __setSFX__

try:
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()

    global __setVolume__

    def buttons(button,posX=0,posY=0,w=35,h=35):
                                 # x>  y^  larg  alt
        if button == '__btnSub__':
            __btnSub__ = pg.Rect(posX, 320, 35, 35)
            return(__btnSub__)
        elif button == '__btnSubSFX__':
            __btnSub__ = pg.Rect(posX, 420, 35, 35)
            return(__btnSub__)
        elif button == '__btnBarMax__':
            __btnBarMax__ = pg.Rect(posX, 320, 200, 35)
            return(__btnBarMax__)
        elif button == '__btnBarMin__':
            __btnBarMin__ = pg.Rect(posX, 320, (20 * (__setVolume__ * 10)), 35)
            return(__btnBarMin__)
        elif button == '__btnBarSFXMax__':
            __btnBarMax__ = pg.Rect(posX, 420, 200, 35)
            return(__btnBarMax__)
        elif button == '__btnBarSFX__':
            __btnBarMin__ = pg.Rect(posX, 420, (20 * (__setSFX__ * 10)), 35)
            return(__btnBarMin__)
        elif button == '__btnSum__':
            __btnSum__ = pg.Rect(posX, 320, 35, 35)
            return(__btnSum__)
        elif button == '__btnSumSFX__':
            __btnSum__ = pg.Rect(posX, 420, 35, 35)
            return(__btnSum__)
        elif button == '__btnLevel__':
            __btnLevel__ = pg.Rect(posX, 320, 35, 35)
            return(__btnLevel__)
        elif button == '__btnKeyboard__':
            __btnKeyboard__ = pg.Rect(posX, posY, w, h)
            return(__btnKeyboard__)

    btnOpc1 = pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnKeyboard__', 900, 427, 21, 21), 3)
    btnOpc2 = pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnKeyboard__', 900, 477, 21, 21), 3)
    btnMinu = pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnSub__', 70))
    btnPlus = pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnSum__', 332))
    btnMinuSFX = pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnSubSFX__', 70))
    btnPlusSFX = pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnSumSFX__', 332))

    level1 = pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnLevel__', 950))
    level2 = pg.draw.rect(app_data.__setScreen__, (114, 114, 114), buttons('__btnLevel__', 1000))
    level3 = pg.draw.rect(app_data.__setScreen__, (114, 114, 114), buttons('__btnLevel__', 1050))
    level4 = pg.draw.rect(app_data.__setScreen__, (114, 114, 114), buttons('__btnLevel__', 1100))

    circulo = pg.draw.rect(app_data.__setScreen__, (0, 0, 255), pg.Rect(480, 320, 120, 120))
    triangulo = pg.draw.rect(app_data.__setScreen__, (255, 0, 0), pg.Rect(585, 420, 120, 120))
    quadrado = pg.draw.rect(app_data.__setScreen__, (252, 204, 0), pg.Rect(680, 320, 120, 120))
    btnBack = pg.draw.rect(app_data.__setScreen__, (0, 0, 0), pg.Rect(60, 35, 140, 42))

    def effectPlay(On=False):
        if On != True:
            effect = drwText('Jogar', app_data.__setFont__(36), (255, 255, 255), app_data.__setScreen__, 582, 460)
            return effect
        else:
            effect = drwText('Jogar', app_data.__setFont__(36), (255, 200, 0), app_data.__setScreen__, 582, 460)
            return effect
    def effectBack(On=False):
        if On != True:
            effect = drwText('VOLTAR', app_data.__setFont__(36), (255, 255, 255), app_data.__setScreen__, 60, 20)
            return effect
        else:
            effect = drwText('VOLTAR', app_data.__setFont__(36), (255, 200, 0), app_data.__setScreen__, 60, 20)
            return effect

    def drwText(text,font,color,surface,x,y):
        textobj = font.render(text,1,color)
        textrect = textobj.get_rect()
        textrect.topleft = (x,y)
        surface.blit(textobj, textrect)
    def drwLOGO(opc=0):

        def drwControlVolume():
            pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnSub__', 70), 3)
            pg.draw.rect(app_data.__setScreen__, (248, 82, 0), buttons('__btnBarMin__', 118))
            pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnBarMax__', 118), 3)
            pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnSum__', 332), 3)

            drwText('Música:', app_data.__setFont__(32), (248, 82, 0), app_data.__setScreen__, 151, 268)
            drwText('Música:', app_data.__setFont__(32), (255, 255, 255), app_data.__setScreen__, 150, 268)
            drwText('-', app_data.__setFont__(32), (255, 255, 255), app_data.__setScreen__, 78, 311)
            drwText('+', app_data.__setFont__(32), (255, 255, 255), app_data.__setScreen__, 340, 311)

            pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnSubSFX__', 70), 3)
            pg.draw.rect(app_data.__setScreen__, (248, 82, 0), buttons('__btnBarSFX__', 118))
            pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnBarSFXMax__', 118), 3)
            pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnSumSFX__', 332), 3)

            drwText('Efeitos:', app_data.__setFont__(32), (248, 82, 0), app_data.__setScreen__, 151, 368)
            drwText('Efeitos:', app_data.__setFont__(32), (255, 255, 255), app_data.__setScreen__, 150, 368)
            drwText('-', app_data.__setFont__(32), (255, 255, 255), app_data.__setScreen__, 78, 411)
            drwText('+', app_data.__setFont__(32), (255, 255, 255), app_data.__setScreen__, 340, 411)

        def drwControlLevel():
            pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnLevel__',950))
            pg.draw.rect(app_data.__setScreen__, (114, 114, 114), buttons('__btnLevel__',1000))
            pg.draw.rect(app_data.__setScreen__, (114, 114, 114), buttons('__btnLevel__',1050))
            pg.draw.rect(app_data.__setScreen__, (114, 114, 114), buttons('__btnLevel__',1100))
            pg.draw.rect(app_data.__setScreen__, (248, 82, 0), buttons('__btnLevel__',950), 3)
            pg.draw.rect(app_data.__setScreen__, (66, 66, 66), buttons('__btnLevel__',1000), 3)
            pg.draw.rect(app_data.__setScreen__, (66, 66, 66), buttons('__btnLevel__',1050), 3)
            pg.draw.rect(app_data.__setScreen__, (66, 66, 66), buttons('__btnLevel__',1100), 3)

            drwText('Dificuldade:', app_data.__setFont__(32), (248, 82, 0), app_data.__setScreen__, 951, 265)
            drwText('Dificuldade:', app_data.__setFont__(32), (255,255,255), app_data.__setScreen__, 950, 265)
            drwText('1', app_data.__setFont__(32), (255, 255, 255), app_data.__setScreen__, 960, 311)
            drwText('2', app_data.__setFont__(32), (255, 255, 255), app_data.__setScreen__, 1010, 311)
            drwText('3', app_data.__setFont__(32), (255, 255, 255), app_data.__setScreen__, 1060, 311)
            drwText('4', app_data.__setFont__(32), (255, 255, 255), app_data.__setScreen__, 1110, 311)
        def drwControlKeybord(opc=0):

            lstSetas = ['Ativo116.png','Ativo117.png','Ativo118.png','Ativo119.png']
            #lstSetas = ['Ativo120.png','Ativo121.png','Ativo122.png','Ativo123.png']
            down = pg.image.load(f'Imagens/Setas/{lstSetas[3]}')
            down = pg.transform.scale(down, (35, 35))
            left = pg.image.load(f'Imagens/Setas/{lstSetas[0]}')
            left = pg.transform.scale(left, (35, 35))
            right = pg.image.load(f'Imagens/Setas/{lstSetas[1]}')
            right = pg.transform.scale(right, (35, 35))
            up = pg.image.load(f'Imagens/Setas/{lstSetas[2]}')
            up = pg.transform.scale(up, (35, 35))

            drwText('Teclas:', app_data.__setFont__(32), (248, 82, 0), app_data.__setScreen__, 968, 368)
            drwText('Teclas:', app_data.__setFont__(32), (255,255,255), app_data.__setScreen__, 967, 368)

            pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnKeyboard__',900,427,21,21),3)
            pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnKeyboard__',950,420))
            pg.draw.rect(app_data.__setScreen__, (248, 82, 0), buttons('__btnKeyboard__',1000,420))
            pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnKeyboard__',1050,420))
            pg.draw.rect(app_data.__setScreen__, (248, 82, 0), buttons('__btnKeyboard__',1100,420))

            drwText('D', app_data.__setFont__(28), (255, 255, 255), app_data.__setScreen__, 957, 414)
            drwText('F', app_data.__setFont__(28), (255, 255, 255), app_data.__setScreen__, 1007, 414)
            drwText('J', app_data.__setFont__(28), (255, 255, 255), app_data.__setScreen__, 1057, 414)
            drwText('K', app_data.__setFont__(28), (255, 255, 255), app_data.__setScreen__, 1107, 414)

            pg.draw.rect(app_data.__setScreen__, (252, 204, 0), buttons('__btnKeyboard__',900,477,21,21),3)
            '''pg.draw.rect(app_data.__setScreen__, (255, 255, 255), buttons('__btnKeyboard__',125,470))
            pg.draw.rect(app_data.__setScreen__, (255,255,255), buttons('__btnKeyboard__',175,470))
            pg.draw.rect(app_data.__setScreen__, (255,255,255), buttons('__btnKeyboard__',225,470))
            pg.draw.rect(app_data.__setScreen__, (255,255,255), buttons('__btnKeyboard__',275,470))'''

            app_data.__setScreen__.blit(down, (950, 470))
            app_data.__setScreen__.blit(left, (1000, 470))
            app_data.__setScreen__.blit(right, (1050, 470))
            app_data.__setScreen__.blit(up, (1100, 470))


            if opc==1:
                pg.draw.rect(app_data.__setScreen__, (248, 82, 0), buttons('__btnKeyboard__',905,482,11,11))
            else:
                pg.draw.rect(app_data.__setScreen__, (248, 82, 0), buttons('__btnKeyboard__', 905, 432, 11, 11))
        app_data.__setScreen__.fill((0, 0, 0))
        app_data.__setScreen__.blit(app_data.__bgVerde__, (0, 0))
        app_data.__setScreen__.blit(app_data.__logoGame__, ((1280 / 2 - app_data.__logoGame__.
                                                      get_width() / 2), 50))

        drwControlVolume()
        drwControlLevel()
        drwControlKeybord(opc)

        app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[0], '__player__'), (480, 320))
        app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[1], '__player__', 0, 140), (565, 420))
        app_data.__setScreen__.blit(app_data.__setPlayer__(__formas__[2], '__player__'), (680, 320))

    def sfxSelect(atv=True):
        # check-off 4-Click
        if atv != True:
            sfx = pg.mixer.Sound("Sounds/check-off.wav")
            sfx.set_volume(app_data.__setSFX__)  # valor entre 0.0 e 1.0
            sfx.play()
        else:
            sfx = pg.mixer.Sound("Sounds/4-Click.wav")
            sfx.set_volume(app_data.__setSFX__)  # valor entre 0.0 e 1.0
            sfx.play()

    def sfxClick(atv=True):
        sfx = pg.mixer.Sound("Sounds/21-Magica.mp3")
        sfx.set_volume(app_data.__setVolume__)  # valor entre 0.0 e 1.0
        sfx.play()

    def call_Options():
        try:
            pg.init()
            screen = app_data.__setScreen__
            app_data.__setTitle__
            app_data.__setIcon__

            running = True
            click = False
            OnB = False
            while running:
                btnOpc1, btnOpc2, btnMinu, btnPlus

                drwLOGO(app_data.__controlKeyboard__)
                coord = pg.mouse.get_pos()
                effectBack(OnB)
                __setCursor__(coord)
                global __setVolume__
                global __setSFX__
                volume_Music = __setVolume__
                volume_SFX = __setSFX__
                mixer.music.set_volume(app_data.__setVolume__)
                for event in pg.event.get():
                    if btnOpc1.collidepoint(coord):
                        app_data.__controlKeyboard__ = 0
                    if btnOpc2.collidepoint(coord):
                        app_data.__controlKeyboard__ = 1
                    if btnBack.collidepoint(coord):
                        OnB = True
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                running = False
                    else:
                        OnB = False
                    if level1.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                            if click:
                                sfxSelect()
                    if level2.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                            if click:
                                sfxSelect(False)
                    if level3.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                            if click:
                                sfxSelect(False)
                    if level4.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                            if click:
                                sfxSelect(False)
                    if circulo.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:sfxClick()

                    if triangulo.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:sfxClick()
                    if quadrado.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:sfxClick()

                    if btnMinu.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                            if click:
                                sfxSelect()
                                if volume_Music > (app_data.__volumeMin__):
                                    __setVolume__ = float("%.1f"%(volume_Music-0.1))
                                    app_data.__setVolume__ = __setVolume__
                                    app_data.lstConfig[5] = __setVolume__
                    if btnPlus.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                            if click:
                                sfxSelect()
                                if volume_Music < (app_data.__volumeMax__):
                                    __setVolume__ = float("%.1f"%(volume_Music+0.1))
                                    app_data.__setVolume__ = __setVolume__
                                    app_data.lstConfig[5] = __setVolume__

                    if btnMinuSFX.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                            if click:
                                sfxSelect()
                                if volume_SFX > (app_data.__volumeMin__):
                                    __setSFX__ = float("%.1f"%(volume_SFX-0.1))
                                    app_data.__setSFX__ = __setSFX__
                                    app_data.lstConfig[6] = __setSFX__
                    if btnPlusSFX.collidepoint(coord):
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                            if click:
                                sfxSelect()
                                if volume_SFX < (app_data.__volumeMax__):
                                    __setSFX__ = float("%.1f"%(volume_SFX+0.1))
                                    app_data.__setSFX__ = __setSFX__
                                    app_data.lstConfig[6] = __setSFX__

                    if event.type == QUIT:
                        __saveConfig__()
                        pg.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            __saveConfig__()
                            running = False
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