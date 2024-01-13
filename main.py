import pygame, sys, random, time, os
from pygame.locals import *

#File Cather
def Photo_Catcher(image_filename):
    return os.path.join(assets_folder, "Los_Fotos", image_filename)
def Sound_Catcher(image_filename):
    return os.path.join(assets_folder, "Los_Sonidos", image_filename)

#Initializing 
pygame.init()

#Klatki Na Sekundę
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Bazowe Kolory
PURPLE = (255,0,255)
CYAN = (0,255,255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)

#Zmienne Okienkowe
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
 
#Czcionki
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 30)
game_over = font.render("Game Over", True, BLACK)
game_won = font.render("Game Won", True, WHITE)

#Źródło Plików
assets_folder = os.path.join(os.getcwd(), "Assets")

#Ładowanie Plików
Background_menu = pygame.image.load(Photo_Catcher("BarraEspanola.png"))
Background = pygame.image.load(Photo_Catcher("EsqueletosEspanoles.jpg"))
Icon = pygame.image.load(Photo_Catcher("Icon.png"))
Hands = pygame.image.load(Photo_Catcher("Hands.png"))
#Słownik Muzyczny
music_path={
    "game": Sound_Catcher("snd_ElMechanico_music.mp3"),
    "menu": Sound_Catcher("snd_SpanishPhonk_music.mp3"),
}

#Tytuł i Ikonka
pygame.display.set_caption('Antumbra','Icon.png')
pygame.display.set_icon(Icon)

#Rozmiar Okienka
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
 
#Obiekty
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

class Play(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Button2-s2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = ((SCREEN_WIDTH/2)-(self.rect.width/2), (SCREEN_HEIGHT/2)-(self.rect.height/2)+40)

#Klasyfikacja
Al = Alpha()
Be = Beta()
De = Delta()
Ta = Tau()
Om = Omicron()
Pl = Play()
 
#Klasyfikacja Grup Teksturowych
all_sprites = pygame.sprite.Group()
dice_sprites = pygame.sprite.Group()
all_sprites.add(Al,Be,De,Ta,Om,Pl)
dice_sprites.add(Al,Be,De,Ta,Om)

#Muzyka zależna od Pokoju
def Music_Changer(game_state):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(music_path[game_state])
    pygame.mixer.music.play(-1)

#Room Startup
game_state="menu"
Music_Changer(game_state)

#Game Loop
while True:
    #Pokój z Menu
    if (game_state =="menu"):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if Pl.rect.x <= mouse_x <= Pl.rect.x+Pl.rect.width and Pl.rect.y <= mouse_y <= Pl.rect.y+Pl.rect.height:
                    game_state="game"

        #Refresher and Renderer
        DISPLAYSURF.blit(Background_menu, (0,0))
        DISPLAYSURF.blit(Pl.image,Pl.rect)
        pygame.display.update()
        FramePerSec.tick(FPS)

    #Pokój z Grą
    if (game_state =="game"):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if Pl.rect.x <= mouse_x <= Pl.rect.x+Pl.rect.width and Pl.rect.y <= mouse_y <= Pl.rect.y+Pl.rect.height:
                    game_state="menu"
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for entity in dice_sprites:
                        entity.roll()

        #Refresher and Renderer
        DISPLAYSURF.blit(Background, (0,0))
        DISPLAYSURF.blit(Hands, (0,484))
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)   

        pygame.display.update()
        FramePerSec.tick(FPS)