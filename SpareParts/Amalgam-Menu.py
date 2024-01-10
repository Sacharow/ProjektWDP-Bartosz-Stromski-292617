import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Button Click Example")

white = (255, 255, 255)
black = (0, 0, 0)

class Omicron(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("k6-dif.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)

Om = Omicron()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Draw everything
    screen.fill(white)
    screen.blit(Om.image,Om.rect)

    # Update display
    pygame.display.flip()
