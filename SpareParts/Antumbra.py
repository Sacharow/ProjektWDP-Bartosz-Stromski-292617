import pygame, sys, pygame_menu
from pygame.locals import *

pygame.init()
surface = pygame.display.set_mode((600, 900))
image=pygame.image.load("FunFactSuperior.png")
image_rect = image.get_rect()
background_color = (255, 255, 255)

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        surface.fill(background_color)
        surface.blit(image,(70,100))
        pygame.display.update()
    pass

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_ORANGE)


menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)




menu.mainloop(surface)
