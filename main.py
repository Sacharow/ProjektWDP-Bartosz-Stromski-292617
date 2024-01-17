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
font_tiny = pygame.font.SysFont("Verdana", 10)
game_over = font.render("Game Over", True, BLACK)
game_won = font.render("Game Won", True, WHITE)


#Źródło Plików
assets_folder = os.path.join(os.getcwd(), "Assets")

#Ładowanie Plików
Background_menu = pygame.image.load(Photo_Catcher("BarraEspanola.png"))
Background_info = pygame.image.load(Photo_Catcher("skeleton_back.png"))
Background_score = pygame.image.load(Photo_Catcher("Score_back.png"))
Background = pygame.image.load(Photo_Catcher("EsqueletosEspanoles.jpg"))
Icon = pygame.image.load(Photo_Catcher("Icon.png"))
PlayButton= pygame.image.load(Photo_Catcher("Play.png"))
HowButton= pygame.image.load(Photo_Catcher("How.png"))
MenuButton= pygame.image.load(Photo_Catcher("Menu.png"))
ScoreButton= pygame.image.load(Photo_Catcher("Score.png"))
Title= pygame.image.load(Photo_Catcher("LosHuesos.png"))
Informacion= pygame.image.load(Photo_Catcher("Informacion.png"))
Puntos= pygame.image.load(Photo_Catcher("Puntos.png"))
#Słownik Muzyczny
music_path={
    "menu": Sound_Catcher("snd_SpanishPhonk_music.mp3"),
    "game": Sound_Catcher("snd_ElMechanico_music.mp3"),
}

#Tytuł i Ikonka
pygame.display.set_caption('Antumbra','Icon.png')
pygame.display.set_icon(Icon)

#Rozmiar Okienka
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Zmienne Wynikowe
wyniki=[0,0,0,0,0]
counter_wyniki=[0,0,0,0,0,0]
suma_wyniki=[0,0,0,0,0,0,0,0,0,0,0,0,0]
final_wynik=[0,0,0,0,0,0,0,0,0,0,0,0,0]

#Zmienne Kostne
roll_amount=2

#Zliczacz
def Zliczacz():
    for i in range(6):
        counter_wyniki[i]=0
        for j in range(5):
            if (wyniki[j]==int(i+1)):
                counter_wyniki[i]+=1

#Kombinacje
def Jedynki():
    suma_wyniki[0]=1*counter_wyniki[0]
def Dwojki():
    suma_wyniki[1]=2*counter_wyniki[1]
def Trojki():
    suma_wyniki[2]=3*counter_wyniki[2]
def Czworki():
    suma_wyniki[3]=4*counter_wyniki[3]
def Piatki():
    suma_wyniki[4]=5*counter_wyniki[4]
def Szostki():
    suma_wyniki[5]=6*counter_wyniki[5]
def ThreeOf():
    for i in range(6):
        if(counter_wyniki[i]>=3):
            suma_wyniki[6]=wyniki[0]+wyniki[1]+wyniki[2]+wyniki[3]+wyniki[4]
            break;
        else:
            suma_wyniki[6]=0
def FourOf():
    for i in range(6):
        if(counter_wyniki[i]>=4):
            suma_wyniki[7]=wyniki[0]+wyniki[1]+wyniki[2]+wyniki[3]+wyniki[4]
            break;
        else:
            suma_wyniki[7]=0
def Full():
    for i in range(6):
        if(counter_wyniki[i]==2):
            for j in range(6):
                if(counter_wyniki[j]==3):
                    suma_wyniki[8]=25
                    break;
        else:
            suma_wyniki[8]=0
def MStraight():
    if(counter_wyniki[0]>0 and counter_wyniki[1]>0 and counter_wyniki[2]>0 and counter_wyniki[3]>0 or counter_wyniki[1]>0 and counter_wyniki[2]>0 and counter_wyniki[3]>0 and counter_wyniki[4]>0 or counter_wyniki[2]>0 and counter_wyniki[3]>0 and counter_wyniki[4]>0 and counter_wyniki[5]>0):
        suma_wyniki[9]=30
    else:
        suma_wyniki[9]=0
def DStraight():
    if(counter_wyniki[0]>0 and counter_wyniki[1]>0 and counter_wyniki[2]>0 and counter_wyniki[3]>0 and counter_wyniki[4]>0 or counter_wyniki[1]>0 and counter_wyniki[2]>0 and counter_wyniki[3]>0 and counter_wyniki[4]>0 and counter_wyniki[5]>0):
        suma_wyniki[10]=40
    else:
        suma_wyniki[10]=0
def Yahtzee():
    for i in range(6):
        if(counter_wyniki[i]==5):
            suma_wyniki[11]=50
            break;
        else:
            suma_wyniki[11]=0
def Szansa():
    suma_wyniki[12]=wyniki[0]+wyniki[1]+wyniki[2]+wyniki[3]+wyniki[4]

#Obiekty Wynikowe
class O_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Je2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,130)

class O_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Dw2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,220)

class O_3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Tr2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,310)

class O_4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Cz2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,400)

class O_5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Pi2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,490)

class O_6(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Sz2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,580)

class O_3X(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("3x2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (510,130)

class O_4X(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("4x2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (510,220)

class O_Full(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Full2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (510,310)

class O_Maly(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Ms2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (510,400)

class O_Duzy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Ds2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (510,490)

class O_Szansa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Szansa2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (510,580)

class O_Yahtzee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Ya2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (268,400)


#Obiekty Kostne
class Alpha(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("k6.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (70, 750)

    def roll(self):
        penumbra = random.randint(1,6)
        wyniki[0]=penumbra
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
        self.rect.topleft = (166, 750)

    def roll(self):
        penumbra = random.randint(1,6)
        wyniki[1]=penumbra
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
        self.rect.topleft = (268, 750)

    def roll(self):
        penumbra = random.randint(1,6)
        wyniki[2]=penumbra
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
        self.rect.topleft = (370, 750)

    def roll(self):
        penumbra = random.randint(1,6)
        wyniki[3]=penumbra
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
        self.rect.topleft = (466, 750)

    def roll(self):
        penumbra = random.randint(1,6)
        wyniki[4]=penumbra
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

#Obiekty Guzikowe
class Play(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = PlayButton
        self.rect = self.image.get_rect()
        self.rect.topleft = ((SCREEN_WIDTH/2)-(self.rect.width/2), (SCREEN_HEIGHT/2)-(self.rect.height/2))

class How(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = HowButton
        self.rect = self.image.get_rect()
        self.rect.topleft = ((SCREEN_WIDTH/2)-(self.rect.width/2), (SCREEN_HEIGHT/2)-(self.rect.height/2)+160)

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = MenuButton
        self.rect = self.image.get_rect()
        self.rect.topleft = ((SCREEN_WIDTH/2)-(self.rect.width/2), (SCREEN_HEIGHT/2)-(self.rect.height/2)-160)

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = ScoreButton
        self.rect = self.image.get_rect()
        self.rect.topleft = ((SCREEN_WIDTH/2)-(self.rect.width/2), (SCREEN_HEIGHT/2)-(self.rect.height/2)+320)

#Klasyfikacja
Al = Alpha()
Be = Beta()
De = Delta()
Ta = Tau()
Om = Omicron()
Pl = Play()
Ho = How()
Me = Menu()
So = Score()

E_1=O_1()
E_2=O_2()
E_3=O_3()
E_4=O_4()
E_5=O_5()
E_6=O_6()
E_3x=O_3X()
E_4x=O_4X()
E_Full=O_Full()
E_Maly=O_Maly()
E_Duzy=O_Duzy()
E_Szansa=O_Szansa()
E_Yahtzee=O_Yahtzee()

#Klasyfikacja Grup Teksturowych i Funkcyjnych
all_sprites = pygame.sprite.Group()
dice_sprites = pygame.sprite.Group()
button_sprites = pygame.sprite.Group()
wyniki_sprites = pygame.sprite.Group()
wyniki_functions=[]

all_sprites.add(Al,Be,De,Ta,Om)
button_sprites.add(Pl,Ho,Me,So)
dice_sprites.add(Al,Be,De,Ta,Om)
wyniki_sprites.add(E_1,E_2,E_3,E_3x,E_4,E_4x,E_5,E_6,E_Duzy,E_Full,E_Maly,E_Szansa,E_Yahtzee)
wyniki_functions=[Zliczacz,Jedynki,Dwojki,Trojki,Czworki,Piatki,Szostki,ThreeOf,FourOf,Full,MStraight,DStraight,Yahtzee,Szansa]

#Muzyka zależna od Pokoju
def Music_Changer(game_state):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(music_path[game_state])
    pygame.mixer.music.play(-1)

#Zapoczątkowanie
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
                    Music_Changer(game_state)
                if Ho.rect.x <= mouse_x <= Ho.rect.x+Ho.rect.width and Ho.rect.y <= mouse_y <= Ho.rect.y+Ho.rect.height:
                    game_state="info"
                if So.rect.x <= mouse_x <= So.rect.x+So.rect.width and So.rect.y <= mouse_y <= So.rect.y+So.rect.height:
                    game_state="score"

        #Refresher and Renderer
        DISPLAYSURF.blit(Background_menu, (0,0))
        DISPLAYSURF.blit(Title, (0,30))
        DISPLAYSURF.blit(Pl.image, Pl.rect) 
        DISPLAYSURF.blit(Ho.image, Ho.rect)  
        DISPLAYSURF.blit(So.image, So.rect)
        pygame.display.update()
        FramePerSec.tick(FPS)

    #Pokój z Score
    if (game_state =="score"):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if Me.rect.x <= mouse_x <= Me.rect.x+Me.rect.width and Me.rect.y <= mouse_y <= Me.rect.y+Me.rect.height:
                    game_state="menu"

        #Refresher and Renderer
        DISPLAYSURF.blit(Background_score, (0,0))
        DISPLAYSURF.blit(Puntos, (0,30))
        DISPLAYSURF.blit(Me.image, Me.rect)  
        pygame.display.update()
        FramePerSec.tick(FPS)

    #Pokój z Info
    if (game_state =="info"):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if Me.rect.x <= mouse_x <= Me.rect.x+Me.rect.width and Me.rect.y <= mouse_y <= Me.rect.y+Me.rect.height:
                    game_state="menu"

        #Refresher and Renderer
        DISPLAYSURF.blit(Background_info, (0,0))
        DISPLAYSURF.blit(Informacion, (0,30))
        DISPLAYSURF.blit(Me.image, Me.rect)  
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
                if Me.rect.x <= mouse_x <= Me.rect.x+Me.rect.width and Me.rect.y <= mouse_y <= Me.rect.y+Me.rect.height:
                    game_state="menu"
                    Music_Changer(game_state)

            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (roll_amount>0):
                        pygame.mixer.Sound(Sound_Catcher("snd_dice_roll.mp3")).play()
                        for entity in dice_sprites:
                            entity.roll()
                        roll_amount-=1
                        for func in wyniki_functions:
                            func()

                if event.key == pygame.K_TAB:
                    roll_amount+=2

        #Refresher and Renderer

        DISPLAYSURF.blit(Background, (0,0))
        wyniki.sort()
        roll_display = font_small.render("Roll Amount: "+str(roll_amount), True, WHITE)
        wyniki_display = font_small.render("Wyniki "+str(wyniki[0])+str(wyniki[1])+str(wyniki[2])+str(wyniki[3])+str(wyniki[4]), True, WHITE)
        counter_display = font_small.render("Counter "+" 1:"+str(counter_wyniki[0])+" 2:"+str(counter_wyniki[1])+" 3:"+str(counter_wyniki[2])+" 4:"+str(counter_wyniki[3])+" 5:"+str(counter_wyniki[4])+" 6:"+str(counter_wyniki[5]), True, WHITE)
        suma_display = font_tiny.render("Suma "+" 1:"+str(suma_wyniki[0])+" 2:"+str(suma_wyniki[1])+" 3:"+str(suma_wyniki[2])+" 4:"+str(suma_wyniki[3])+" 5:"+str(suma_wyniki[4])+" 6:"+str(suma_wyniki[5])+" ThreeOf:"+str(suma_wyniki[6])+" FourOf:"+str(suma_wyniki[7])+" Full:"+str(suma_wyniki[8])+" MStraight:"+str(suma_wyniki[9])+" DStraight:"+str(suma_wyniki[10])+" Yahtzee"+str(suma_wyniki[11])+" Szansa:"+str(suma_wyniki[12]), True, WHITE)
        DISPLAYSURF.blit(roll_display, (70,20))
        DISPLAYSURF.blit(wyniki_display,(70,50))
        DISPLAYSURF.blit(counter_display,(70,80))
        DISPLAYSURF.blit(suma_display,(30,115))
        DISPLAYSURF.blit(Me.image, Me.rect) 
        for entity in dice_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
        for entity in wyniki_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)   

        pygame.display.update()
        FramePerSec.tick(FPS)