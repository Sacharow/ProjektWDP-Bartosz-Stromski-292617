import pygame, sys, random, time, os
from pygame.locals import *

#SPIS TREŚCI WZGLĘDEM LINIJEK ----------------------------------------------------------------------------------------------------------------

# SPIS TREŚCI
# FUNKCJE ZBIERAJĄCE PLIKI Z FOLDERÓW PODRZĘDNYCH
# ZAPOCZĄTKOWANIE ALFA
# KLATKI NA SEKUNDE
# BAZOWE KOLORY
# ZMIENNE OKIENKOWE - ROZDZIELCZOŚĆ
# CZCIONKI
# ŹRÓDŁA PLIKÓW
# ŁADOWANIE CZĘŚCI PLIKÓW
# SŁOWNIK MUZYCZNY
# TYTUŁ I IKONA
# ROZMIAR OKIENKA / PROGRAMU
# ZMIENNE WYNIKOWE / TABLICOWE
# WCZYTYWANIE WYNIKÓW Z PLIKU
# ZMIENNE POMNIEJSZE
# ZLICZACZ - FUNCKJA ZLICZAJĄC ILOŚĆ
# JEDNOŚCI I KOMBINACJE
# OBIEKTY WYNIKOWE
# OBIEKTY KOSTNE
# OBIEKTY GUZIKOWE
# KLASYFIKACJA
# KLASYFIKACJA GRUP TEKSTUROWYCH I FUNKCJYCH
# FUNKCJA ZMIENNOŚCI MUZYKI WZGLĘDEM POKOJU
# ZAPOCZĄTKOWANIE BETA
# PĘTLA GRY
# POKÓJ MENU
#   NAJEŻDZANIE NA GUZIK ZMIENIA KOLOR
#   WYŁĄCZENIE GRY
#   AKTYWACJA GUZIKÓW PRZEJŚCIA
#   WYPIS DANYCH
# POKÓJ SCORE
#   NAJEŻDZANIE NA GUZIK ZMIENIA KOLOR
#   WYŁĄCZENIE GRY
#   AKTYWACJA GUZIKÓW PRZEJŚCIA
#   WYPIS DANYCH
# POKÓJ INFO
#   NAJEŻDZANIE NA GUZIK ZMIENIA KOLOR
#   WYŁĄCZENIE GRY
#   AKTYWACJA GUZIKÓW PRZEJŚCIA
#   WYPIS DANYCH
# POKÓJ GAME
#   CAŁKOWITY RESET W PRZYPADKU PONOWNEJ GRY
#   NAJEŻDZANIE NA GUZIK ZMIENIA KOLOR
#   #WYŁĄCZENIE GRY
#   AKTYWACJA GUZIKÓW PRZEJŚCIA
#   BLOKADA KOŚCI
#   BLOKADA WYNIKU
#   BONUS DODATKOWEGO YAHTZEE
#   KONIEC GRY - MINEŁO 13 RUND
#   BONUS SUMA JEDNOSTEK WIEKSZA RÓWNA 62
#   SUMOWANIE WYNIKU I PODMIANA WYNIKU DO PLIKU
#   ZMIANA POKOJU _NA POKÓJ Z WYNIKAMI
#   PRZERZUT KOŚCI I JEGO PODRZĘDNE
#   WYPIS DANYCH

#FUNKCJE ZBIERAJĄCE PLIKI Z FOLDERÓW PODRZĘDNYCH ----------------------------------------------------------------------------------------------------------------
def Photo_Catcher(image_filename):
    return os.path.join(assets_folder, "Los_Fotos", image_filename)
def Sound_Catcher(image_filename):
    return os.path.join(assets_folder, "Los_Sonidos", image_filename)

#ZAPOCZĄTKOWANIE ALFA ----------------------------------------------------------------------------------------------------------------
pygame.init()

#KLATKI NA SEKUNDE ----------------------------------------------------------------------------------------------------------------
FPS = 60
FramePerSec = pygame.time.Clock()
 
#BAZOWE KOLORY ----------------------------------------------------------------------------------------------------------------
PURPLE = (255,0,255)
CYAN = (0,255,255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

#ZMIENNE OKIENKOWE - ROZDZIELCZOŚĆ ----------------------------------------------------------------------------------------------------------------
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
 
#CZCIONKI ----------------------------------------------------------------------------------------------------------------
font = pygame.font.SysFont("Comic Sans MS", 80)
font.set_bold(True)
font_med = pygame.font.SysFont("Comic Sans MS", 60)
font_med.set_bold(True)
font_small = pygame.font.SysFont("Comic Sans MS", 30)
font_tiny = pygame.font.SysFont("Comic Sans MS", 10)


#ŹRÓDŁA PLIKÓW ----------------------------------------------------------------------------------------------------------------
assets_folder = os.path.join(os.getcwd(), "Assets")

#ŁADOWANIE CZĘŚCI PLIKÓW ----------------------------------------------------------------------------------------------------------------
Background_menu = pygame.image.load(Photo_Catcher("back7.png"))
Background_info = pygame.image.load(Photo_Catcher("skele-back.png"))
Background_score = pygame.image.load(Photo_Catcher("skele-back2.png"))
Background = pygame.image.load(Photo_Catcher("skele-back3.png"))
Icon = pygame.image.load(Photo_Catcher("Icon.png"))
Title= pygame.image.load(Photo_Catcher("title.png"))

#SŁOWNIK MUZYCZNY ----------------------------------------------------------------------------------------------------------------
music_path={
    "menu": Sound_Catcher("snd_SpanishPhonk_music.mp3"),
    "info": Sound_Catcher("snd_SpanishPhonk_music.mp3"),
    "score": Sound_Catcher("snd_SpanishPhonk_music.mp3"),
    "game": Sound_Catcher("snd_ElMechanico_music.mp3"),
}

#TYTUŁ I IKONA ----------------------------------------------------------------------------------------------------------------
pygame.display.set_caption('Antumbra','Icon.png')
pygame.display.set_icon(Icon)

#ROZMIAR OKIENKA / PROGRAMU ----------------------------------------------------------------------------------------------------------------
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#ZMIENNE WYNIKOWE / TABLICOWE ----------------------------------------------------------------------------------------------------------------
wyniki=[0,0,0,0,0]
numer=[0,0,0,0,0]
lock=[0,0,0,0,0]
wynik_lock=[0,0,0,0,0,0,0,0,0,0,0,0,0]
counter_wyniki=[0,0,0,0,0,0]
suma_wyniki=[0,0,0,0,0,0,0,0,0,0,0,0,0]
final_wyniki=[0,0,0,0,0,0,0,0,0,0,0,0,0]

#WCZYTYWANIE WYNIKÓW Z PLIKU ----------------------------------------------------------------------------------------------------------------
f=open("wynik.txt","r")
for i in range(4):
    linia=f.readline().strip()
    if i==0:
        FIRST=int(linia)
    if i==1:
        SECOND=int(linia)
    if i==2:
        THIRD=int(linia)
    if i==3:
        FINAL=int(linia)


#ZMIENNE POMNIEJSZE ----------------------------------------------------------------------------------------------------------------
roll_amount=3
bonus=0
counter_time=0

# ZLICZACZ - FUNCKJA ZLICZAJĄC ILOŚĆ ----------------------------------------------------------------------------------------------------------------
def Zliczacz():
    for i in range(6):
        counter_wyniki[i]=0
        for j in range(5):
            if (wyniki[j]==int(i+1)):
                counter_wyniki[i]+=1

#JEDNOŚCI I KOMBINACJE ----------------------------------------------------------------------------------------------------------------
def Jedynki():
    if wynik_lock[0]==0:
        suma_wyniki[0]=1*counter_wyniki[0]
def Dwojki():
    if wynik_lock[1]==0:
        suma_wyniki[1]=2*counter_wyniki[1]
def Trojki():
    if wynik_lock[2]==0:
        suma_wyniki[2]=3*counter_wyniki[2]
def Czworki():
    if wynik_lock[3]==0:
        suma_wyniki[3]=4*counter_wyniki[3]
def Piatki():
    if wynik_lock[4]==0:
        suma_wyniki[4]=5*counter_wyniki[4]
def Szostki():
    if wynik_lock[5]==0:
        suma_wyniki[5]=6*counter_wyniki[5]
def ThreeOf():
    if wynik_lock[6]==0:
        for i in range(6):
            if(counter_wyniki[i]>=3):
                suma_wyniki[6]=wyniki[0]+wyniki[1]+wyniki[2]+wyniki[3]+wyniki[4]
                break;
            else:
                suma_wyniki[6]=0
def FourOf():
    if wynik_lock[7]==0:
        for i in range(6):
            if(counter_wyniki[i]>=4):
                suma_wyniki[7]=wyniki[0]+wyniki[1]+wyniki[2]+wyniki[3]+wyniki[4]
                break;
            else:
                suma_wyniki[7]=0
def Full():
    if wynik_lock[8]==0:
        for i in range(6):
            if(counter_wyniki[i]==2):
                for j in range(6):
                    if(counter_wyniki[j]==3):
                        suma_wyniki[8]=25
                        break;
                    else:
                        suma_wyniki[8]=0
def MStraight():
    if wynik_lock[9]==0:
        if(counter_wyniki[0]>0 and counter_wyniki[1]>0 and counter_wyniki[2]>0 and counter_wyniki[3]>0 or counter_wyniki[1]>0 and counter_wyniki[2]>0 and counter_wyniki[3]>0 and counter_wyniki[4]>0 or counter_wyniki[2]>0 and counter_wyniki[3]>0 and counter_wyniki[4]>0 and counter_wyniki[5]>0):
            suma_wyniki[9]=30
        else:
            suma_wyniki[9]=0
def DStraight():
    if wynik_lock[10]==0:
        if(counter_wyniki[0]>0 and counter_wyniki[1]>0 and counter_wyniki[2]>0 and counter_wyniki[3]>0 and counter_wyniki[4]>0 or counter_wyniki[1]>0 and counter_wyniki[2]>0 and counter_wyniki[3]>0 and counter_wyniki[4]>0 and counter_wyniki[5]>0):
            suma_wyniki[10]=40
        else:
            suma_wyniki[10]=0
def Yahtzee():
    if wynik_lock[11]==0:
        for i in range(6):
            if(counter_wyniki[i]==5):
                suma_wyniki[11]=50
                break;
            else:
                suma_wyniki[11]=0
def Szansa():
    if wynik_lock[12]==0:
        suma_wyniki[12]=wyniki[0]+wyniki[1]+wyniki[2]+wyniki[3]+wyniki[4]

# OBIEKTY WYNIKOWE ----------------------------------------------------------------------------------------------------------------
class O_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("11.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,180)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("11.png"))
class O_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("22.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,270)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("22.png"))
class O_3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("33.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,360)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("33.png"))
class O_4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("44.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,450)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("44.png"))
class O_5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("55.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,540)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("55.png"))
class O_6(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("66.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (10,630)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("66.png"))
class O_3X(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("3xx.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (510,180)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("3xx.png"))
class O_4X(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("4xx.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (510,270)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("4xx.png"))
class O_Full(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("ff.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (510,360)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("ff.png"))
class O_Maly(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("abc.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (510,450)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("abc.png"))
class O_Duzy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("abc-up.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (510,540)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("abc-up.png"))
class O_Szansa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("ss.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (510,630)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("ss.png"))
class O_Yahtzee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("yy.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (268,400)
    def restart(self):
        self.image = pygame.image.load(Photo_Catcher("yy.png"))


#OBIEKTY KOSTNE ----------------------------------------------------------------------------------------------------------------
class Alpha(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("00r.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (70, 750)

    def roll(self):
        if lock[0]==0:
            penumbra = random.randint(1,6)
            wyniki[0]=penumbra
            numer[0]=penumbra
            if penumbra == 1:
                self.image = pygame.image.load(Photo_Catcher("11r.png"))
            if penumbra == 2:
                self.image = pygame.image.load(Photo_Catcher("22r.png"))
            if penumbra == 3:
                self.image = pygame.image.load(Photo_Catcher("33r.png"))
            if penumbra == 4:
                self.image = pygame.image.load(Photo_Catcher("44r.png"))
            if penumbra == 5:
                self.image = pygame.image.load(Photo_Catcher("55r.png"))
            if penumbra == 6:
                self.image = pygame.image.load(Photo_Catcher("66r.png"))
        
    def change(self):
        if numer[0]>0:
            if lock[0]==0:
                if numer[0]==1:
                    self.image = pygame.image.load(Photo_Catcher("1-1.png"))
                if numer[0]==2:
                    self.image = pygame.image.load(Photo_Catcher("2-2.png"))
                if numer[0]==3:
                    self.image = pygame.image.load(Photo_Catcher("3-3.png"))
                if numer[0]==4:
                    self.image = pygame.image.load(Photo_Catcher("4-4.png"))
                if numer[0]==5:
                    self.image = pygame.image.load(Photo_Catcher("5-5.png"))
                if numer[0]==6:
                    self.image = pygame.image.load(Photo_Catcher("6-6.png"))
                lock[0]=1
            elif lock[0]==1:
                if numer[0]==1:
                    self.image = pygame.image.load(Photo_Catcher("11r.png"))
                if numer[0]==2:
                    self.image = pygame.image.load(Photo_Catcher("22r.png"))
                if numer[0]==3:
                    self.image = pygame.image.load(Photo_Catcher("33r.png"))
                if numer[0]==4:
                    self.image = pygame.image.load(Photo_Catcher("44r.png"))
                if numer[0]==5:
                    self.image = pygame.image.load(Photo_Catcher("55r.png"))
                if numer[0]==6:
                    self.image = pygame.image.load(Photo_Catcher("66r.png"))
                lock[0]=0
class Beta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("00r.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (166, 750)

    def roll(self):
        if lock[1]==0:
            penumbra = random.randint(1,6)
            wyniki[1]=penumbra
            numer[1]=penumbra
            if penumbra == 1:
                self.image = pygame.image.load(Photo_Catcher("11r.png"))
            if penumbra == 2:
                self.image = pygame.image.load(Photo_Catcher("22r.png"))
            if penumbra == 3:
                self.image = pygame.image.load(Photo_Catcher("33r.png"))
            if penumbra == 4:
                self.image = pygame.image.load(Photo_Catcher("44r.png"))
            if penumbra == 5:
                self.image = pygame.image.load(Photo_Catcher("55r.png"))
            if penumbra == 6:
                self.image = pygame.image.load(Photo_Catcher("66r.png"))
        
    def change(self):
        if numer[1]>0:
            if lock[1]==0:
                if numer[1]==1:
                    self.image = pygame.image.load(Photo_Catcher("1-1.png"))
                if numer[1]==2:
                    self.image = pygame.image.load(Photo_Catcher("2-2.png"))
                if numer[1]==3:
                    self.image = pygame.image.load(Photo_Catcher("3-3.png"))
                if numer[1]==4:
                    self.image = pygame.image.load(Photo_Catcher("4-4.png"))
                if numer[1]==5:
                    self.image = pygame.image.load(Photo_Catcher("5-5.png"))
                if numer[1]==6:
                    self.image = pygame.image.load(Photo_Catcher("6-6.png"))
                lock[1]=1
            elif lock[1]==1:
                if numer[1]==1:
                    self.image = pygame.image.load(Photo_Catcher("11r.png"))
                if numer[1]==2:
                    self.image = pygame.image.load(Photo_Catcher("22r.png"))
                if numer[1]==3:
                    self.image = pygame.image.load(Photo_Catcher("33r.png"))
                if numer[1]==4:
                    self.image = pygame.image.load(Photo_Catcher("44r.png"))
                if numer[1]==5:
                    self.image = pygame.image.load(Photo_Catcher("55r.png"))
                if numer[1]==6:
                    self.image = pygame.image.load(Photo_Catcher("66r.png"))
                lock[1]=0
class Delta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("00r.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (268, 750)

    def roll(self):
        if lock[2]==0:
            penumbra = random.randint(1,6)
            wyniki[2]=penumbra
            numer[2]=penumbra
            if penumbra == 1:
                self.image = pygame.image.load(Photo_Catcher("11r.png"))
            if penumbra == 2:
                self.image = pygame.image.load(Photo_Catcher("22r.png"))
            if penumbra == 3:
                self.image = pygame.image.load(Photo_Catcher("33r.png"))
            if penumbra == 4:
                self.image = pygame.image.load(Photo_Catcher("44r.png"))
            if penumbra == 5:
                self.image = pygame.image.load(Photo_Catcher("55r.png"))
            if penumbra == 6:
                self.image = pygame.image.load(Photo_Catcher("66r.png"))
        
    def change(self):
        if numer[2]>0:
            if lock[2]==0:
                if numer[2]==1:
                    self.image = pygame.image.load(Photo_Catcher("1-1.png"))
                if numer[2]==2:
                    self.image = pygame.image.load(Photo_Catcher("2-2.png"))
                if numer[2]==3:
                    self.image = pygame.image.load(Photo_Catcher("3-3.png"))
                if numer[2]==4:
                    self.image = pygame.image.load(Photo_Catcher("4-4.png"))
                if numer[2]==5:
                    self.image = pygame.image.load(Photo_Catcher("5-5.png"))
                if numer[2]==6:
                    self.image = pygame.image.load(Photo_Catcher("6-6.png"))
                lock[2]=1
            elif lock[2]==1:
                if numer[2]==1:
                    self.image = pygame.image.load(Photo_Catcher("11r.png"))
                if numer[2]==2:
                    self.image = pygame.image.load(Photo_Catcher("22r.png"))
                if numer[2]==3:
                    self.image = pygame.image.load(Photo_Catcher("33r.png"))
                if numer[2]==4:
                    self.image = pygame.image.load(Photo_Catcher("44r.png"))
                if numer[2]==5:
                    self.image = pygame.image.load(Photo_Catcher("55r.png"))
                if numer[2]==6:
                    self.image = pygame.image.load(Photo_Catcher("66r.png"))
                lock[2]=0
class Tau(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("00r.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (370, 750)

    def roll(self):
        if lock[3]==0:
            penumbra = random.randint(1,6)
            wyniki[3]=penumbra
            numer[3]=penumbra
            if penumbra == 1:
                self.image = pygame.image.load(Photo_Catcher("11r.png"))
            if penumbra == 2:
                self.image = pygame.image.load(Photo_Catcher("22r.png"))
            if penumbra == 3:
                self.image = pygame.image.load(Photo_Catcher("33r.png"))
            if penumbra == 4:
                self.image = pygame.image.load(Photo_Catcher("44r.png"))
            if penumbra == 5:
                self.image = pygame.image.load(Photo_Catcher("55r.png"))
            if penumbra == 6:
                self.image = pygame.image.load(Photo_Catcher("66r.png"))
        
    def change(self):
        if numer[3]>0:
            if lock[3]==0:
                if numer[3]==1:
                    self.image = pygame.image.load(Photo_Catcher("1-1.png"))
                if numer[3]==2:
                    self.image = pygame.image.load(Photo_Catcher("2-2.png"))
                if numer[3]==3:
                    self.image = pygame.image.load(Photo_Catcher("3-3.png"))
                if numer[3]==4:
                    self.image = pygame.image.load(Photo_Catcher("4-4.png"))
                if numer[3]==5:
                    self.image = pygame.image.load(Photo_Catcher("5-5.png"))
                if numer[3]==6:
                    self.image = pygame.image.load(Photo_Catcher("6-6.png"))
                lock[3]=1
            elif lock[3]==1:
                if numer[3]==1:
                    self.image = pygame.image.load(Photo_Catcher("11r.png"))
                if numer[3]==2:
                    self.image = pygame.image.load(Photo_Catcher("22r.png"))
                if numer[3]==3:
                    self.image = pygame.image.load(Photo_Catcher("33r.png"))
                if numer[3]==4:
                    self.image = pygame.image.load(Photo_Catcher("44r.png"))
                if numer[3]==5:
                    self.image = pygame.image.load(Photo_Catcher("55r.png"))
                if numer[3]==6:
                    self.image = pygame.image.load(Photo_Catcher("66r.png"))
                lock[3]=0
class Omicron(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("00r.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (466, 750)

    def roll(self):
        if lock[4]==0:
            penumbra = random.randint(1,6)
            wyniki[4]=penumbra
            numer[4]=penumbra
            if penumbra == 1:
                self.image = pygame.image.load(Photo_Catcher("11r.png"))
            if penumbra == 2:
                self.image = pygame.image.load(Photo_Catcher("22r.png"))
            if penumbra == 3:
                self.image = pygame.image.load(Photo_Catcher("33r.png"))
            if penumbra == 4:
                self.image = pygame.image.load(Photo_Catcher("44r.png"))
            if penumbra == 5:
                self.image = pygame.image.load(Photo_Catcher("55r.png"))
            if penumbra == 6:
                self.image = pygame.image.load(Photo_Catcher("66r.png"))
        
    def change(self):
        if numer[4]>0:
            if lock[4]==0:
                if numer[4]==1:
                    self.image = pygame.image.load(Photo_Catcher("1-1.png"))
                if numer[4]==2:
                    self.image = pygame.image.load(Photo_Catcher("2-2.png"))
                if numer[4]==3:
                    self.image = pygame.image.load(Photo_Catcher("3-3.png"))
                if numer[4]==4:
                    self.image = pygame.image.load(Photo_Catcher("4-4.png"))
                if numer[4]==5:
                    self.image = pygame.image.load(Photo_Catcher("5-5.png"))
                if numer[4]==6:
                    self.image = pygame.image.load(Photo_Catcher("6-6.png"))
                lock[4]=1
            elif lock[4]==1:
                if numer[4]==1:
                    self.image = pygame.image.load(Photo_Catcher("11r.png"))
                if numer[4]==2:
                    self.image = pygame.image.load(Photo_Catcher("22r.png"))
                if numer[4]==3:
                    self.image = pygame.image.load(Photo_Catcher("33r.png"))
                if numer[4]==4:
                    self.image = pygame.image.load(Photo_Catcher("44r.png"))
                if numer[4]==5:
                    self.image = pygame.image.load(Photo_Catcher("55r.png"))
                if numer[4]==6:
                    self.image = pygame.image.load(Photo_Catcher("66r.png"))
                lock[4]=0


#OBIEKTY GUZIKOWE ----------------------------------------------------------------------------------------------------------------
class Play(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Play2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = ((SCREEN_WIDTH/2)-(self.rect.width/2), 350)
class How(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Rules2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = ((SCREEN_WIDTH/2)-(self.rect.width/2), 500)
class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Menu3.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = ((SCREEN_WIDTH/2)-(self.rect.width/2), (SCREEN_HEIGHT/2)-(self.rect.height/2)-400)
class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Score2.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = ((SCREEN_WIDTH/2)-(self.rect.width/2), 650)
class MiniHow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Rules3.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (SCREEN_WIDTH/2-212, 18)
class MiniScore(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(Photo_Catcher("Score3.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (SCREEN_WIDTH/2+84, 18)

#KLASYFIKACJA ----------------------------------------------------------------------------------------------------------------
Al = Alpha()
Be = Beta()
De = Delta()
Ta = Tau()
Om = Omicron()
Pl = Play()
Ho = How()
Me = Menu()
So = Score()
Mho = MiniHow()
Mso = MiniScore()

W1=O_1()
W2=O_2()
W3=O_3()
W4=O_4()
W5=O_5()
W6=O_6()
W7=O_3X()
W8=O_4X()
W9=O_Full()
W10=O_Maly()
W11=O_Duzy()
W12=O_Yahtzee()
W13=O_Szansa()

#KLASYFIKACJA GRUP TEKSTUROWYCH I FUNKCJYCH ----------------------------------------------------------------------------------------------------------------
all_sprites = pygame.sprite.Group()
dice_sprites = pygame.sprite.Group()
button_sprites = pygame.sprite.Group()
wyniki_sprites = pygame.sprite.Group()
wyniki_functions=[]

all_sprites.add(Al,Be,De,Ta,Om)
button_sprites.add(Pl,Ho,Me,So,Mho,Mso)
dice_sprites.add(Al,Be,De,Ta,Om)
wyniki_sprites.add(W1,W2,W3,W4,W5,W6,W7,W8,W9,W10,W11,W12,W13)
wyniki_functions=[Zliczacz,Jedynki,Dwojki,Trojki,Czworki,Piatki,Szostki,ThreeOf,FourOf,Full,MStraight,DStraight,Yahtzee,Szansa]

#FUNKCJA ZMIENNOŚCI MUZYKI WZGLĘDEM POKOJU ----------------------------------------------------------------------------------------------------------------
def Music_Changer(game_state):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(music_path[game_state])
    pygame.mixer.music.play(-1)

#ZAPOCZĄTKOWANIE BETA
game_state="menu"
Music_Changer(game_state)

#PĘTLA GRY
while True:
    #POKÓJ MENU ----------------------------------------------------------------------------------------------------------------
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if (game_state =="menu"):
        for event in pygame.event.get():
            #NAJEŻDZANIE NA GUZIK ZMIENIA KOLOR ----------------------------------------------------------------------------------------------------------------
            if Pl.rect.x <= mouse_x <= Pl.rect.x+Pl.rect.width and Pl.rect.y <= mouse_y <= Pl.rect.y+Pl.rect.height:
                Pl.image=pygame.image.load(Photo_Catcher("Play2-2.png"))
            else:
                Pl.image=pygame.image.load(Photo_Catcher("Play2.png"))
            if Ho.rect.x <= mouse_x <= Ho.rect.x+Ho.rect.width and Ho.rect.y <= mouse_y <= Ho.rect.y+Ho.rect.height:
                Ho.image=pygame.image.load(Photo_Catcher("Rules2-2.png"))
            else:
                Ho.image=pygame.image.load(Photo_Catcher("Rules2.png"))
            if So.rect.x <= mouse_x <= So.rect.x+So.rect.width and So.rect.y <= mouse_y <= So.rect.y+So.rect.height:
                So.image=pygame.image.load(Photo_Catcher("Score2-2.png"))
            else:
                So.image=pygame.image.load(Photo_Catcher("Score2.png"))
            #WYŁĄCZENIE GRY ----------------------------------------------------------------------------------------------------------------
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #AKTYWACJA GUZIKÓW PRZEJŚCIA ----------------------------------------------------------------------------------------------------------------
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Pl.rect.x <= mouse_x <= Pl.rect.x+Pl.rect.width and Pl.rect.y <= mouse_y <= Pl.rect.y+Pl.rect.height:
                    game_state="game"
                    Pl.image=pygame.image.load(Photo_Catcher("Play2.png"))
                    Music_Changer(game_state)
                if Ho.rect.x <= mouse_x <= Ho.rect.x+Ho.rect.width and Ho.rect.y <= mouse_y <= Ho.rect.y+Ho.rect.height:
                    game_state="info"
                    Ho.image=pygame.image.load(Photo_Catcher("Rules2.png"))
                if So.rect.x <= mouse_x <= So.rect.x+So.rect.width and So.rect.y <= mouse_y <= So.rect.y+So.rect.height:
                    game_state="score"
                    So.image=pygame.image.load(Photo_Catcher("Score2.png"))

        #WYPIS DANYCH ----------------------------------------------------------------------------------------------------------------
        DISPLAYSURF.blit(Background_menu, (0,0))
        DISPLAYSURF.blit(Title, (25,30))
        DISPLAYSURF.blit(Pl.image, Pl.rect) 
        DISPLAYSURF.blit(Ho.image, Ho.rect)  
        DISPLAYSURF.blit(So.image, So.rect)
        pygame.display.update()
        FramePerSec.tick(FPS)

    #POKÓJ SCORE ----------------------------------------------------------------------------------------------------------------
    if (game_state =="score"):
        for event in pygame.event.get():
            #NAJEŻDZANIE NA GUZIK ZMIENIA KOLOR ----------------------------------------------------------------------------------------------------------------
            if Me.rect.x <= mouse_x <= Me.rect.x+Me.rect.width and Me.rect.y <= mouse_y <= Me.rect.y+Me.rect.height:
                Me.image=pygame.image.load(Photo_Catcher("Menu3-3.png"))
            else:
                Me.image=pygame.image.load(Photo_Catcher("Menu3.png"))
            #WYŁĄCZENIE GRY ----------------------------------------------------------------------------------------------------------------
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #AKTYWACJA GUZIKÓW PRZEJŚCIA ----------------------------------------------------------------------------------------------------------------
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if Me.rect.x <= mouse_x <= Me.rect.x+Me.rect.width and Me.rect.y <= mouse_y <= Me.rect.y+Me.rect.height:
                    game_state="menu"
                    Me.image=pygame.image.load(Photo_Catcher("Menu3.png"))

        #WYPIS DANYCH ----------------------------------------------------------------------------------------------------------------
        FINAL_display= font_med.render("LAST SCORE",True,WHITE)
        FINAL_display2= font_med.render("LAST SCORE",True,BLACK)
        FINAL_display_rect=FINAL_display.get_rect(center=(SCREEN_WIDTH/2,580))
        FINAL_display_rect2=FINAL_display2.get_rect(center=(SCREEN_WIDTH/2+8,588))

        FINAL_Number_display= font_med.render(str(FINAL),True,WHITE)
        FINAL_Number_display_rect=FINAL_Number_display.get_rect(center=(SCREEN_WIDTH/2,680))
        FINAL_Number_display2= font_med.render(str(FINAL),True,BLACK)
        FINAL_Number_display_rect2=FINAL_Number_display2.get_rect(center=(SCREEN_WIDTH/2+5,685))

        FIRST_display= font_med.render("THE BEST SCORES",True,WHITE)
        FIRST_display2= font_med.render("THE BEST SCORES",True,BLACK)
        FIRST_display_rect=FIRST_display.get_rect(center=(SCREEN_WIDTH/2,140))
        FIRST_display_rect2=FIRST_display2.get_rect(center=(SCREEN_WIDTH/2+8,148))

        FIRST_Number_display= font_med.render(str(FIRST),True,WHITE)
        FIRST_Number_display_rect=FIRST_Number_display.get_rect(center=(SCREEN_WIDTH/2,240))
        FIRST_Number_display2= font_med.render(str(FIRST),True,BLACK)
        FIRST_Number_display_rect2=FIRST_Number_display2.get_rect(center=(SCREEN_WIDTH/2+5,245))

        SECOND_Number_display= font_med.render(str(SECOND),True,WHITE)
        SECOND_Number_display_rect=SECOND_Number_display.get_rect(center=(SCREEN_WIDTH/2,340))
        SECOND_Number_display2= font_med.render(str(SECOND),True,BLACK)
        SECOND_Number_display_rect2=SECOND_Number_display2.get_rect(center=(SCREEN_WIDTH/2+5,345))

        THIRD_Number_display= font_med.render(str(THIRD),True,WHITE)
        THIRD_Number_display_rect=THIRD_Number_display.get_rect(center=(SCREEN_WIDTH/2,440))
        THIRD_Number_display2= font_med.render(str(THIRD),True,BLACK)
        THIRD_Number_display_rect2=THIRD_Number_display2.get_rect(center=(SCREEN_WIDTH/2+5,445))

        DISPLAYSURF.blit(Background_score, (0,0))
        DISPLAYSURF.blit(FINAL_Number_display2,FINAL_Number_display_rect2.topleft)
        DISPLAYSURF.blit(FINAL_Number_display,FINAL_Number_display_rect.topleft)
        DISPLAYSURF.blit(FINAL_display2,FINAL_display_rect2.topleft)
        DISPLAYSURF.blit(FINAL_display,FINAL_display_rect.topleft)
        DISPLAYSURF.blit(FIRST_Number_display2,FIRST_Number_display_rect2.topleft)
        DISPLAYSURF.blit(FIRST_Number_display,FIRST_Number_display_rect.topleft)
        DISPLAYSURF.blit(FIRST_display2,FIRST_display_rect2.topleft)
        DISPLAYSURF.blit(FIRST_display,FIRST_display_rect.topleft)
        DISPLAYSURF.blit(SECOND_Number_display2,SECOND_Number_display_rect2.topleft)
        DISPLAYSURF.blit(SECOND_Number_display,SECOND_Number_display_rect.topleft)
        DISPLAYSURF.blit(THIRD_Number_display2,THIRD_Number_display_rect2.topleft)
        DISPLAYSURF.blit(THIRD_Number_display,THIRD_Number_display_rect.topleft)

        DISPLAYSURF.blit(Me.image, Me.rect)  
        pygame.display.update()
        FramePerSec.tick(FPS)

    #POKÓJ INFO ----------------------------------------------------------------------------------------------------------------
    if (game_state =="info"):
        for event in pygame.event.get():
            #NAJEŻDZANIE NA GUZIK ZMIENIA KOLOR ----------------------------------------------------------------------------------------------------------------
            if Me.rect.x <= mouse_x <= Me.rect.x+Me.rect.width and Me.rect.y <= mouse_y <= Me.rect.y+Me.rect.height:
                Me.image=pygame.image.load(Photo_Catcher("Menu3-3.png"))
            else:
                Me.image=pygame.image.load(Photo_Catcher("Menu3.png"))
            #WYŁĄCZENIE GRY ----------------------------------------------------------------------------------------------------------------
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #AKTYWACJA GUZIKÓW PRZEJŚCIA ----------------------------------------------------------------------------------------------------------------
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if Me.rect.x <= mouse_x <= Me.rect.x+Me.rect.width and Me.rect.y <= mouse_y <= Me.rect.y+Me.rect.height:
                    game_state="menu"
                    Me.image=pygame.image.load(Photo_Catcher("Menu3.png"))

        #WYPIS DANYCH ----------------------------------------------------------------------------------------------------------------
        DISPLAYSURF.blit(Background_info, (0,0))
        DISPLAYSURF.blit(pygame.image.load(Photo_Catcher("instrukcja7.png")),(-15,0))
        DISPLAYSURF.blit(Me.image, Me.rect)  
        pygame.display.update()
        FramePerSec.tick(FPS)

    #POKÓJ GAME ----------------------------------------------------------------------------------------------------------------
    if (game_state =="game"):
        #CAŁKOWITY RESET W PRZYPADKU PONOWNEJ GRY ----------------------------------------------------------------------------------------------------------------
        if counter_time==13:
            wyniki=[0,0,0,0,0]
            numer=[0,0,0,0,0]
            lock=[0,0,0,0,0]
            wynik_lock=[0,0,0,0,0,0,0,0,0,0,0,0,0]
            counter_wyniki=[0,0,0,0,0,0]
            suma_wyniki=[0,0,0,0,0,0,0,0,0,0,0,0,0]
            final_wyniki=[0,0,0,0,0,0,0,0,0,0,0,0,0]
            roll_amount=3
            counter_time=0
            for entity in wyniki_sprites:
                entity.restart()

        for event in pygame.event.get():
            #NAJEŻDZANIE NA GUZIK ZMIENIA KOLOR ----------------------------------------------------------------------------------------------------------------
            if Me.rect.x <= mouse_x <= Me.rect.x+Me.rect.width and Me.rect.y <= mouse_y <= Me.rect.y+Me.rect.height:
                Me.image=pygame.image.load(Photo_Catcher("Menu3-3.png"))
            else:
                Me.image=pygame.image.load(Photo_Catcher("Menu3.png"))
            if Mho.rect.x <= mouse_x <= Mho.rect.x+Mho.rect.width and Mho.rect.y <= mouse_y <= Mho.rect.y+Mho.rect.height:
                Mho.image=pygame.image.load(Photo_Catcher("Rules3-3.png"))
            else:
                Mho.image=pygame.image.load(Photo_Catcher("Rules3.png"))
            if Mso.rect.x <= mouse_x <= Mso.rect.x+Mso.rect.width and Mso.rect.y <= mouse_y <= Mso.rect.y+Mso.rect.height:
                Mso.image=pygame.image.load(Photo_Catcher("Score3-3.png"))
            else:
                Mso.image=pygame.image.load(Photo_Catcher("Score3.png"))
            #WYŁĄCZENIE GRY ----------------------------------------------------------------------------------------------------------------
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #AKTYWACJA GUZIKÓW PRZEJŚCIA ----------------------------------------------------------------------------------------------------------------
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if Me.rect.x <= mouse_x <= Me.rect.x+Me.rect.width and Me.rect.y <= mouse_y <= Me.rect.y+Me.rect.height:
                    game_state="menu"
                    Music_Changer(game_state)
                if Mho.rect.x <= mouse_x <= Mho.rect.x+Mho.rect.width and Mho.rect.y <= mouse_y <= Mho.rect.y+Mho.rect.height:
                    game_state="info"
                    Mho.image=pygame.image.load(Photo_Catcher("Rules3.png"))
                    Music_Changer(game_state)
                if Mso.rect.x <= mouse_x <= Mso.rect.x+Mso.rect.width and Mso.rect.y <= mouse_y <= Mso.rect.y+Mso.rect.height:
                    game_state="score"
                    Mso.image=pygame.image.load(Photo_Catcher("Score3.png"))
                    Music_Changer(game_state)
                #BLOKADA KOŚCI ----------------------------------------------------------------------------------------------------------------
                if (roll_amount<3):
                    for entity in dice_sprites:
                        if entity.rect.x <= mouse_x <= entity.rect.x+entity.rect.width and entity.rect.y <= mouse_y <= entity.rect.y+entity.rect.height:
                            entity.change()

                #BLOKADA WYNIKU ----------------------------------------------------------------------------------------------------------------
                if (roll_amount<3):
                    for i in range(1,14):
                        Element=globals()[f'W{i}']
                        if Element.rect.x <= mouse_x <= Element.rect.x+Element.rect.width and Element.rect.y <= mouse_y <= Element.rect.y+Element.rect.height and wynik_lock[i-1]==0:
                            wynik_lock[i-1]=1
                            counter_time+=1
                            Element.image = pygame.image.load(Photo_Catcher("00.png"))
                            #BONUS DODATKOWEGO YAHTZEE ----------------------------------------------------------------------------------------------------------------
                            if i<7:
                                if counter_wyniki[i-1]==5 and final_wyniki[11]==50:
                                    bonus+=50
                                    #print(bonus)
                            final_wyniki[i-1]=suma_wyniki[i-1]
                            for entity in dice_sprites:
                                entity.image = pygame.image.load(Photo_Catcher("0.png"))
                            for i in range (0,5):
                                lock[i]=0
                            roll_amount=3
                            #KONIEC GRY - MINEŁO 13 RUND ----------------------------------------------------------------------------------------------------------------
                            if(counter_time==13):
                                FINAL=0
                                #BONUS SUMA JEDNOSTEK WIEKSZA RÓWNA 62 ----------------------------------------------------------------------------------------------------------------
                                if(final_wyniki[0]+final_wyniki[1]+final_wyniki[2]+final_wyniki[3]+final_wyniki[4]+final_wyniki[5]>=62):
                                    FINAL=FINAL+35
                                FINAL+=bonus
                                #SUMOWANIE WYNIKU I PODMIANA WYNIKU DO PLIKU ----------------------------------------------------------------------------------------------------------------
                                for i in range(0,13):
                                    FINAL=FINAL+final_wyniki[i]
                                if FINAL>FIRST:
                                    THIRD=SECOND
                                    SECOND=FIRST
                                    FIRST=FINAL
                                elif FINAL>SECOND:
                                    THIRD=SECOND
                                    SECOND=FINAL
                                elif FINAL>THIRD:
                                    THIRD=FINAL
                                f=open("wynik.txt","w")
                                for i in range(4):
                                    if i==0:
                                        f.writelines(str(FIRST)+"\n")
                                    if i==1:
                                        f.writelines(str(SECOND)+"\n")
                                    if i==2:
                                        f.writelines(str(THIRD)+"\n")
                                    if i==3:
                                        f.writelines(str(FINAL)+"\n")
                                #ZMIANA POKOJU _NA POKÓJ Z WYNIKAMI ----------------------------------------------------------------------------------------------------------------
                                game_state="score"
                                Music_Changer(game_state)

            #PRZERZUT KOŚCI I JEGO PODRZĘDNE ----------------------------------------------------------------------------------------------------------------
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (roll_amount>0):
                        if (lock[0]==0 or lock[1]==0 or lock[2]==0 or lock[3]==0 or lock[4]==0):
                            pygame.mixer.Sound(Sound_Catcher("snd_dice_roll.mp3")).play()
                            for entity in dice_sprites:
                                entity.roll()
                            roll_amount-=1
                            for func in wyniki_functions:
                                func()
    
        #WYPIS DANYCH ----------------------------------------------------------------------------------------------------------------
        DISPLAYSURF.blit(Background, (0,0))
        for i in range(0,6):
            DISPLAYSURF.blit(pygame.image.load(Photo_Catcher("00p.png")),(90,180+i*90))
        s0=font_small.render(str(suma_wyniki[0]),True,YELLOW)
        DISPLAYSURF.blit(s0,(120,195))
        s1=font_small.render(str(suma_wyniki[1]),True,YELLOW)
        DISPLAYSURF.blit(s1,(120,285))
        s2=font_small.render(str(suma_wyniki[2]),True,YELLOW)
        DISPLAYSURF.blit(s2,(120,375))
        s3=font_small.render(str(suma_wyniki[3]),True,YELLOW)
        DISPLAYSURF.blit(s3,(120,465))
        s4=font_small.render(str(suma_wyniki[4]),True,YELLOW)
        DISPLAYSURF.blit(s4,(120,555))
        s5=font_small.render(str(suma_wyniki[5]),True,YELLOW)
        DISPLAYSURF.blit(s5,(120,645))
        for i in range(0,6):
            DISPLAYSURF.blit(pygame.image.load(Photo_Catcher("00p.png")),(430,180+i*90))
        s6=font_small.render(str(suma_wyniki[6]),True,YELLOW)
        DISPLAYSURF.blit(s6,(455,195))
        s7=font_small.render(str(suma_wyniki[7]),True,YELLOW)
        DISPLAYSURF.blit(s7,(455,285))
        s8=font_small.render(str(suma_wyniki[8]),True,YELLOW)
        DISPLAYSURF.blit(s8,(455,375))
        s9=font_small.render(str(suma_wyniki[9]),True,YELLOW)
        DISPLAYSURF.blit(s9,(455,465))
        s10=font_small.render(str(suma_wyniki[10]),True,YELLOW)
        DISPLAYSURF.blit(s10,(455,555))
        s11=font_small.render(str(suma_wyniki[12]),True,YELLOW)
        DISPLAYSURF.blit(s11,(455,645))
        DISPLAYSURF.blit(pygame.image.load(Photo_Catcher("00p.png")),(268,330))
        s12=font_small.render(str(suma_wyniki[11]),True,YELLOW)
        DISPLAYSURF.blit(s12,(298,344))
        DISPLAYSURF.blit(Me.image, Me.rect) 
        DISPLAYSURF.blit(Mho.image, Mho.rect)
        DISPLAYSURF.blit(Mso.image, Mso.rect)
        for entity in dice_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
        for entity in wyniki_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)   

        pygame.display.update()
        FramePerSec.tick(FPS)