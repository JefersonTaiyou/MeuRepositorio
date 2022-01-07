import pygame,traceback, sys
from datetime import datetime
from pygame.locals import *
from sys import exit
from pygame.time import *
from Classes import app_data
from Classes.app_data import __setCursor__
from Classes.Opcoes import drwText

try:
    pygame.init()
    tela = app_data.__setScreen__
    LARGURA,ALTURA = app_data.__largura__,app_data.__altura__
    app_data.__setTitle__
    app_data.__setIcon__

    btnBack = pygame.draw.rect(app_data.__setScreen__, (0, 0, 0), pygame.Rect(20, 631, 140, 42))

    def effectBack(On=False):
        if On != True:
            effect = drwText('VOLTAR', app_data.__setFont__(36), (255, 255, 255), app_data.__setScreen__, 20, 631)
            return effect
        else:
            effect = drwText('VOLTAR', app_data.__setFont__(36), (255, 200, 0), app_data.__setScreen__, 20, 631)
            return effect
    class bg(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('Imagens/Creditos/BG-Ingrid.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/BG-Jeff.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/BG-Natan.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/BG-Yan.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/BG-Guilherme.png'))
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (1280, 720))
            self.rect = self.image.get_rect()
            self.rect.topleft = 0, 0
            self.animar = False

        def animation(self):
            self.animar = True

        def update(self):
            if self.animar == True:
                self.atual = self.atual + 0.009
                if self.atual >= len(self.sprites):
                    self.atual = 0
                    self.animar = False
                self.image = self.sprites[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (1280, 720))
    class img1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('Imagens/Creditos/yan200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/guilherme200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/ingrid200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/jeferson200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/natan200.png'))
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.image.set_alpha(50)
            self.rect = self.image.get_rect()
            self.rect.topleft = 85, 50
            self.animar = False

        def animation(self):
            self.animar = True

        def update(self):
            if self.animar == True:
                self.atual = self.atual + 0.009
                if self.atual >= len(self.sprites):
                    self.atual = 0
                    self.animar = False
                self.image = self.sprites[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_alpha(50)
    class img2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('Imagens/Creditos/guilherme200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/ingrid200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/jeferson200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/natan200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/yan200.png'))
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.image.set_alpha(50)
            self.rect = self.image.get_rect()
            self.rect.topleft = 300, 185
            self.animar = False

        def animation(self):
            self.animar = True

        def update(self):
            if self.animar == True:
                self.atual = self.atual + 0.009
                if self.atual >= len(self.sprites):
                    self.atual = 0
                    self.animar = False
                self.image = self.sprites[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_alpha(50)
    class img3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('Imagens/Creditos/ingrid250.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/jeferson250.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/natan250.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/yan250.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/guilherme250.png'))
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (250, 250))
            self.image.set_alpha(200)
            self.rect = self.image.get_rect()
            self.rect.topleft = 515, 235
            self.animar = False

        def animation(self):
            self.animar = True

        def update(self):
            if self.animar == True:
                self.atual = self.atual + 0.009
                if self.atual >= len(self.sprites):
                    self.atual = 0
                    self.animar = False
                self.image = self.sprites[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (250, 250))
                self.image.set_alpha(200)
    class img4(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('Imagens/Creditos/jeferson200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/natan200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/yan200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/guilherme200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/ingrid200.png'))
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.image.set_alpha(50)
            self.rect = self.image.get_rect()
            self.rect.topleft = 780, 185
            self.animar = False

        def animation(self):
            self.animar = True

        def update(self):
            if self.animar == True:
                self.atual = self.atual + 0.009
                if self.atual >= len(self.sprites):
                    self.atual = 0
                    self.animar = False
                self.image = self.sprites[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_alpha(50)
    class img5(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('Imagens/Creditos/natan200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/yan200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/guilherme200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/ingrid200.png'))
            self.sprites.append(pygame.image.load('Imagens/Creditos/jeferson200.png'))
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.image.set_alpha(50)
            self.rect = self.image.get_rect()
            self.rect.topleft = 995, 50
            self.animar = False

        def animation(self):
            self.animar = True

        def update(self):
            if self.animar == True:
                self.atual = self.atual + 0.009
                if self.atual >= len(self.sprites):
                    self.atual = 0
                    self.animar = False
                self.image = self.sprites[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.image.set_alpha(50)

    def call_credits():
        todas_sprites1 = pygame.sprite.Group()
        Img1 = img1()
        todas_sprites1.add(Img1)
        todas_sprites2 = pygame.sprite.Group()
        Img2 = img2()
        todas_sprites2.add(Img2)
        todas_sprites3 = pygame.sprite.Group()
        Img3 = img3()
        todas_sprites3.add(Img3)
        todas_sprites4 = pygame.sprite.Group()
        Img4 = img4()
        todas_sprites4.add(Img4)
        todas_sprites5 = pygame.sprite.Group()
        Img5 = img5()
        todas_sprites5.add(Img5)
        todas_sprites6 = pygame.sprite.Group()
        Bg = bg()
        todas_sprites6.add(Bg)

        running = True
        OnB = False
        while running:
            tela.fill((0, 0, 0))

            todas_sprites6.draw(tela)
            todas_sprites6.update()
            todas_sprites1.draw(tela)
            todas_sprites1.update()
            todas_sprites2.draw(tela)
            todas_sprites2.update()
            todas_sprites3.draw(tela)
            todas_sprites3.update()
            todas_sprites4.draw(tela)
            todas_sprites4.update()
            todas_sprites5.draw(tela)
            todas_sprites5.update()
            tela.blit(app_data.__logoGame__, ((app_data.__largura__ / 2 - app_data.__logo__.
                                                                get_width() / 2), 50))
            coord = pygame.mouse.get_pos()
            effectBack(OnB)
            __setCursor__(coord)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if Bg.atual == 0:
                    Bg.animation()
                    Img1.animation()
                    Img2.animation()
                    Img3.animation()
                    Img4.animation()
                    Img5.animation()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if btnBack.collidepoint(coord):
                    OnB = True
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            running = False
                else:
                    OnB = False
                if event.type == MOUSEBUTTONDOWN:
                    posX, posY = pygame.mouse.get_pos()
                    if 20 <= posX <= 160:
                        if 630 <= posY <= 680:
                            running = False

            pygame.display.flip()

except OSError:
    err = traceback.format_exc()
    data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    with open('Dados/Execucoes.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{data_hora} Game - OS Error:\n {err}\n\n')
        arquivo.close()
except ValueError:
    err = traceback.format_exc()
    data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    with open('Dados/Execucoes.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{data_hora} Game - Value Error:\n {err}\n\n')
        arquivo.close()
except BaseException:
    err = traceback.format_exc()
    data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    with open('Dados/Execucoes.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{data_hora} Game - Unexpected:\n {err}\n\n')
        arquivo.close()
    raise