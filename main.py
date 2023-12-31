import pygame, sys
from pygame.locals import *
import random, time
import os 




#Initializing 
pygame.init()

#Frames Per Second
FPS = 60
FramePerSec = pygame.time.Clock()
 
#LOS COLORES 
PURPLE = (255,0,255)
CYAN = (0,255,255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)

#LOS VARIABLES ADICIONALES
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
 
#VER LAS LENGUAS DEL ORDENADOR
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 30)
game_over = font.render("Game Over", True, BLACK)
game_won = font.render("Game Won", True, WHITE)

#Pliki
Background = pygame.image.load("spr_EsqueletosEspanoles_back.jpg")
Icon = pygame.image.load("Icon.png")
K6 = pygame.image.load('k6.png')
Hands = pygame.image.load('spr_hands.png')

#Tytuł i Ikona
pygame.display.set_caption('Antumbra','Icon.png')
pygame.display.set_icon(Icon)

#Rozdzielczość
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
 
#Klasy Kości
class Alpha(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("k6.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (70, 600)

    def reroll(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_1]:
            pygame.mixer.Sound("snd_dice_roll.mp3").play()
            penumbra = random.randint(1,6)
            if penumbra == 1:
                self.image = pygame.image.load("k6-1.png")
            if penumbra == 2:
                self.image = pygame.image.load("k6-2.png")
            if penumbra == 3:
                self.image = pygame.image.load("k6-3.png")
            if penumbra == 4:
                self.image = pygame.image.load("k6-4.png")
            if penumbra == 5:
                self.image = pygame.image.load("k6-5.png")
            if penumbra == 6:
                self.image = pygame.image.load("k6-6.png")

class Beta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("k6.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (166, 600)

    def reroll(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_2]:
            pygame.mixer.Sound("snd_dice_roll.mp3").play()
            penumbra = random.randint(1,6)
            if penumbra == 1:
                self.image = pygame.image.load("k6-1.png")
            if penumbra == 2:
                self.image = pygame.image.load("k6-2.png")
            if penumbra == 3:
                self.image = pygame.image.load("k6-3.png")
            if penumbra == 4:
                self.image = pygame.image.load("k6-4.png")
            if penumbra == 5:
                self.image = pygame.image.load("k6-5.png")
            if penumbra == 6:
                self.image = pygame.image.load("k6-6.png")

class Delta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("k6.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (268, 600)

    def reroll(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_3]:
            pygame.mixer.Sound("snd_dice_roll.mp3").play()
            penumbra = random.randint(1,6)
            if penumbra == 1:
                self.image = pygame.image.load("k6-1.png")
            if penumbra == 2:
                self.image = pygame.image.load("k6-2.png")
            if penumbra == 3:
                self.image = pygame.image.load("k6-3.png")
            if penumbra == 4:
                self.image = pygame.image.load("k6-4.png")
            if penumbra == 5:
                self.image = pygame.image.load("k6-5.png")
            if penumbra == 6:
                self.image = pygame.image.load("k6-6.png")

class Tau(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("k6.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (370, 600)

    def reroll(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_4]:
            pygame.mixer.Sound("snd_dice_roll.mp3").play()
            penumbra = random.randint(1,6)
            if penumbra == 1:
                self.image = pygame.image.load("k6-1.png")
            if penumbra == 2:
                self.image = pygame.image.load("k6-2.png")
            if penumbra == 3:
                self.image = pygame.image.load("k6-3.png")
            if penumbra == 4:
                self.image = pygame.image.load("k6-4.png")
            if penumbra == 5:
                self.image = pygame.image.load("k6-5.png")
            if penumbra == 6:
                self.image = pygame.image.load("k6-6.png")

class Omicron(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("k6.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (466, 600)

    def reroll(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_5]:
            pygame.mixer.Sound("snd_dice_roll.mp3").play()
            penumbra = random.randint(1,6)
            if penumbra == 1:
                self.image = pygame.image.load("k6-1.png")
            if penumbra == 2:
                self.image = pygame.image.load("k6-2.png")
            if penumbra == 3:
                self.image = pygame.image.load("k6-3.png")
            if penumbra == 4:
                self.image = pygame.image.load("k6-4.png")
            if penumbra == 5:
                self.image = pygame.image.load("k6-5.png")
            if penumbra == 6:
                self.image = pygame.image.load("k6-6.png")


#Klasyfikacja
Al = Alpha()
Be = Beta()
De = Delta()
Ta = Tau()
Om = Omicron()
 
#Klasyfikacja Grup Teksturowych
all_sprites = pygame.sprite.Group()
all_sprites.add(Al,Be,De,Ta,Om)


#Music
pygame.mixer.music.load("snd_ElMechanico_music.mp3")
pygame.mixer.music.play(-1)

#Game Loop
while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Refresher and Renderer
    DISPLAYSURF.blit(Background, (0,0))
    DISPLAYSURF.blit(Hands, (0,484))
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.reroll()
    pygame.display.update()
    FramePerSec.tick(FPS)