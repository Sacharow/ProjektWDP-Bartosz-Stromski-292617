import pygame
import sys

pygame.init()

# Ustawienia okna gry
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Przykład Pygame KEYDOWN")

# Kolor tła
background_color = (255, 255, 255)

# Ustawienia gracza
player_color = (0, 128, 255)
player_size = 50
player_x = (width - player_size) // 2
player_y = height - player_size - 10

# Główna pętla gry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Sprawdź, który klawisz został naciśnięty
            if event.key == pygame.K_LEFT:
                player_x -= 10
            elif event.key == pygame.K_RIGHT:
                player_x += 10
            elif event.key == pygame.K_UP:
                player_y -= 10
            elif event.key == pygame.K_DOWN:
                player_y += 10

    # Rysowanie tła
    screen.fill(background_color)

    # Rysowanie gracza
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # Odświeżenie ekranu
    pygame.display.flip()

# Zakończenie gry
pygame.quit()
sys.exit()