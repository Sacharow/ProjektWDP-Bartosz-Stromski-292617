import pygame, sys
from pygame.locals import *
import random, time
import os 




#Initializing 
pygame.init()
#pygame.mixer.init() 

#Setting up FPS 
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
background = pygame.image.load("spr_dice_back.png")
Icon = pygame.image.load("Icon.png")
k6 = pygame.image.load('k6.png')

#Tytuł i Ikona
pygame.display.set_caption('Antumbra','Icon.png')
pygame.display.set_icon(Icon)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
 
class Alpha(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
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
        self.rect = self.image.get_rect()
        self.rect.topleft = (70, 600)
class Beta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
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
        self.rect = self.image.get_rect()
        self.rect.topleft = (166, 600)
class Delta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
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
        self.rect = self.image.get_rect()
        self.rect.topleft = (268, 600)
class Tau(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
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
        self.rect = self.image.get_rect()
        self.rect.topleft = (370, 600)
class Omicron(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
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
        self.rect = self.image.get_rect()
        self.rect.topleft = (466, 600)

#Setting up Sprites        
Al = Alpha()
Be = Beta()
De = Delta()
Ta = Tau()
Om = Omicron()
 
#Creating Sprites Groups
all_sprites = pygame.sprite.Group()
all_sprites.add(Al,Be,De,Ta,Om)


#Music
pygame.mixer.music.load("snd_back_music.mp3")
pygame.mixer.music.play(-1)

#Game Loop
while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    #Refresher and Renderer
    DISPLAYSURF.blit(background, (0,0))
    all_sprites.draw(DISPLAYSURF)
    pygame.display.update()
    FramePerSec.tick(FPS)