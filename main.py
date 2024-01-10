import pygame, sys, random, time, os
from pygame.locals import *

#File Cather
def Photo_Catcher(image_filename):
    return os.path.join(assets_folder, "Los_Fotos", image_filename)
def Sound_Catcher(image_filename):
    return os.path.join(assets_folder, "Los_Sonidos", image_filename)

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

#EL ARCHIVO
assets_folder = os.path.join(os.getcwd(), "Assets")

#El Archivos del archivo
Background = pygame.image.load(Photo_Catcher("EsqueletosEspanoles.jpg"))
Icon = pygame.image.load(Photo_Catcher("Icon.png"))
Hands = pygame.image.load(Photo_Catcher("Hands.png"))

#EL TITULO Y MAS
pygame.display.set_caption('Antumbra','Icon.png')
pygame.display.set_icon(Icon)

#Los Dimensiones
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
 
#Los Huesos :3
class Alpha(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("k6.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (70, 600)

    def roll(self):
        pygame.mixer.Sound(Sound_Catcher("snd_dice_roll.mp3")).play()
        penumbra = random.randint(1,6)
        if penumbra == 1:
            self.image = pygame.image.load(Photo_Catcher("k6-1.png"))
        if penumbra == 2:
            self.image = pygame.image.load(Photo_Catcher("k6-2.png"))
        if penumbra == 3:
            self.image = pygame.image.load(Photo_Catcher("k6-3.png"))
        if penumbra == 4:
            self.image = pygame.image.load(Photo_Catcher("k6-4.png"))
        if penumbra == 5:
            self.image = pygame.image.load(Photo_Catcher("k6-5.png"))
        if penumbra == 6:
            self.image = pygame.image.load(Photo_Catcher("k6-6.png"))

class Beta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("k6.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (166, 600)

    def roll(self):
        pygame.mixer.Sound(Sound_Catcher("snd_dice_roll.mp3")).play()
        penumbra = random.randint(1,6)
        if penumbra == 1:
            self.image = pygame.image.load(Photo_Catcher("k6-1.png"))
        if penumbra == 2:
            self.image = pygame.image.load(Photo_Catcher("k6-2.png"))
        if penumbra == 3:
            self.image = pygame.image.load(Photo_Catcher("k6-3.png"))
        if penumbra == 4:
            self.image = pygame.image.load(Photo_Catcher("k6-4.png"))
        if penumbra == 5:
            self.image = pygame.image.load(Photo_Catcher("k6-5.png"))
        if penumbra == 6:
            self.image = pygame.image.load(Photo_Catcher("k6-6.png"))

class Delta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("k6.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (268, 600)

    def roll(self):
        pygame.mixer.Sound(Sound_Catcher("snd_dice_roll.mp3")).play()
        penumbra = random.randint(1,6)
        if penumbra == 1:
            self.image = pygame.image.load(Photo_Catcher("k6-1.png"))
        if penumbra == 2:
            self.image = pygame.image.load(Photo_Catcher("k6-2.png"))
        if penumbra == 3:
            self.image = pygame.image.load(Photo_Catcher("k6-3.png"))
        if penumbra == 4:
            self.image = pygame.image.load(Photo_Catcher("k6-4.png"))
        if penumbra == 5:
            self.image = pygame.image.load(Photo_Catcher("k6-5.png"))
        if penumbra == 6:
            self.image = pygame.image.load(Photo_Catcher("k6-6.png"))

class Tau(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("k6.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (370, 600)

    def roll(self):
        pygame.mixer.Sound(Sound_Catcher("snd_dice_roll.mp3")).play()
        penumbra = random.randint(1,6)
        if penumbra == 1:
            self.image = pygame.image.load(Photo_Catcher("k6-1.png"))
        if penumbra == 2:
            self.image = pygame.image.load(Photo_Catcher("k6-2.png"))
        if penumbra == 3:
            self.image = pygame.image.load(Photo_Catcher("k6-3.png"))
        if penumbra == 4:
            self.image = pygame.image.load(Photo_Catcher("k6-4.png"))
        if penumbra == 5:
            self.image = pygame.image.load(Photo_Catcher("k6-5.png"))
        if penumbra == 6:
            self.image = pygame.image.load(Photo_Catcher("k6-6.png"))

class Omicron(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("k6.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (466, 600)

    def roll(self):
        pygame.mixer.Sound(Sound_Catcher("snd_dice_roll.mp3")).play()
        penumbra = random.randint(1,6)
        if penumbra == 1:
            self.image = pygame.image.load(Photo_Catcher("k6-1.png"))
        if penumbra == 2:
            self.image = pygame.image.load(Photo_Catcher("k6-2.png"))
        if penumbra == 3:
            self.image = pygame.image.load(Photo_Catcher("k6-3.png"))
        if penumbra == 4:
            self.image = pygame.image.load(Photo_Catcher("k6-4.png"))
        if penumbra == 5:
            self.image = pygame.image.load(Photo_Catcher("k6-5.png"))
        if penumbra == 6:
            self.image = pygame.image.load(Photo_Catcher("k6-6.png"))


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
pygame.mixer.music.load(Sound_Catcher("snd_ElMechanico_music.mp3"))
pygame.mixer.music.play(-1)

#Game Loop
while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                for entity in all_sprites:
                    entity.roll()

    #Refresher and Renderer
    DISPLAYSURF.blit(Background, (0,0))
    DISPLAYSURF.blit(Hands, (0,484))
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)   

    pygame.display.update()
    FramePerSec.tick(FPS)