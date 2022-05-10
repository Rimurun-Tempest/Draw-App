import pygame
import sys
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()

game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Line Drawing Game")

game_run = True

prev_point = None
mouse_mode = 0
game_window.fill((0,0,0))
clock = pygame.time.Clock()
FPS = 120


def draw(event):
    global prev_point
    curr_point = event.pos
    if prev_point is not None:
        pygame.draw.aaline(game_window, random_color, prev_point, curr_point, 3)
    prev_point = curr_point

def eraser(event):
    pygame.draw.circle(game_window,BLACK,event.pos,10)
    # pygame.draw.aaline(game_window, (0,0,0), prev_point, curr_point, 10)


def clear():
    global prev_point
    game_window.fill((0,0,0))
    prev_point = None


while game_run:

    
    for event in pygame.event.get():
        # print(event)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_mode = 1
            random_color = (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_mode = 2

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_mode = 0
            prev_point = None

        if event.type == pygame.MOUSEMOTION and mouse_mode == 1:
            draw(event)
        if event.type == pygame.MOUSEMOTION and mouse_mode == 2:
            eraser(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                clear()
            elif event.key == pygame.K_UP:
                FPS += 60
            elif event.key == pygame.K_DOWN:
                FPS = 30

        if event.type == pygame.QUIT:
            game_run = False

    pygame.display.update()
    # FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()
