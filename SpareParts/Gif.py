import pygame
import os
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
width, height = 1200, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animacja GIF w Pygame")

white = (255,255,255)

font = pygame.font.SysFont("Verdana", 60, bold=True)

# Ścieżka do folderu z klatkami
L_frames_folder = "Assets\Gif\L"
R_frames_folder = "Assets\Gif\R"
S_frames_folder = "Assets\Gif\S"

# Lista plików w folderze
L_frame_files = sorted([f for f in os.listdir(L_frames_folder) if f.endswith(".png")])
R_frame_files = sorted([f for f in os.listdir(R_frames_folder) if f.endswith(".png")])
S_frame_files = sorted([f for f in os.listdir(S_frames_folder) if f.endswith(".png")])

# Lista klatek
L_frames = [pygame.image.load(os.path.join(L_frames_folder, f)) for f in L_frame_files]
R_frames = [pygame.image.load(os.path.join(R_frames_folder, f)) for f in R_frame_files]
S_frames = [pygame.image.load(os.path.join(S_frames_folder, f)) for f in S_frame_files]

# Ustawienia animacji
L_frame_index = 0
L_frame_rate = 2
R_frame_index = 0
R_frame_rate = 2
S_frame_index = 0
S_frame_rate = 2
clock = pygame.time.Clock()

# Główna pętla programu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rysowanie aktualnej klatki
    screen.fill(white)
    screen.blit(S_frames[S_frame_index], (410, 100))
    screen.blit(L_frames[L_frame_index], (780, 90))
    screen.blit(R_frames[R_frame_index], (0, 90))

    # Aktualizacja indeksu klatki
    L_frame_index = (L_frame_index + 1) % len(L_frames)
    R_frame_index = (R_frame_index + 1) % len(R_frames)
    S_frame_index = (S_frame_index + 1) % len(S_frames)

    text = font.render("SANS", True, (0, 0, 0))

    # Pozycjonowanie tekstu na ekranie
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height // 2 -180)

    # Narysuj tekst na ekranie
    screen.blit(text, text_rect)
    # Odświeżenie ekranu

    pygame.display.flip()

    # Ustawienie częstotliwości klatek
    clock.tick(L_frame_rate)