import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Button Click Example")

white = (255, 255, 255)
black = (0, 0, 0)
cyan = (0,255,255)
red = (255,0,0)

class Omicron(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("button.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = ((width/2)-(self.rect.width/2), (height/2)-(self.rect.height/2))

Om = Omicron()
game_state="menu"

while True:
    if (game_state =="menu"):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if Om.rect.x <= mouse_x <= Om.rect.x+Om.rect.width and Om.rect.y <= mouse_y <= Om.rect.y+Om.rect.height:
                    print("Przycisk został naciśnięty!")
                    game_state="game"
        screen.fill(cyan)
        screen.blit(Om.image,Om.rect)

        pygame.display.flip()
    if (game_state =="game"):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(red)
        pygame.display.flip()
