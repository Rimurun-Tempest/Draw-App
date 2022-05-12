import pygame
import sys


WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (19, 69, 99)

pygame.init()

game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
icon = pygame.image.load('Assets/draw.png')
pygame.display.set_caption("Draw V2")
pygame.display.set_icon(icon)
game_window.fill((WHITE))

font_komika = pygame.font.SysFont(None, 60)
background = pygame.image.load('Assets/background.jpg').convert()

clock = pygame.time.Clock()
FPS = 60

# Drawing Text on Screen 

def draw_text(text, font, surface, color, x, y):
    textobj = font.render(text, False, color, WHITE)
    textobj.set_colorkey(WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    game_window.blit(textobj, textrect)
    return textobj, textrect

# Creating a Surface for chosen button
def chsn(surface, alpha = 40, color = BLACK):
    glare = pygame.Surface(surface.get_size())
    glare.set_alpha(alpha)
    glare.fill(color)
    return glare

# Rendering the chosen button surface
def btn_chsn(mx, my, click, btn_rect, btn_srf, glr_srf):
    if btn_rect.collidepoint(mx, my):
        game_window.blit(btn_srf, btn_rect)
        game_window.blit(glr_srf, btn_rect)
        if click:
            return True
    elif ~btn_rect.collidepoint(mx, my):
        game_window.blit(btn_srf, btn_rect)
    return False

# Main Menu

def main_menu():

    # Title Image
    title = pygame.image.load("Assets/Title.png").convert_alpha()
    title.set_colorkey(WHITE)
    background.blit(title, (140, 50))

    game_window.blit(background, (0, 0))
    BUTTON_X = 220

    # Draw Button
    draw_text1, draw_button = draw_text('Draw', font_komika,
                                        game_window, CYAN, BUTTON_X, 170)

    # Options Button
    opt_text, opt_button = draw_text('Options', font_komika,
                                     game_window, CYAN, BUTTON_X, 230)

    # About Button
    abt_text, abt_button = draw_text('About', font_komika,
                                     game_window, CYAN, BUTTON_X, 290)

    click = False
    pygame.display.update()

    glare_draw = chsn(draw_text1)
    glare_opt = chsn(opt_text)
    glare_abt = chsn(abt_text)

    while True:

        # Mouse Positon
        mx, my = pygame.mouse.get_pos()
        game_window.blit(background, (0, 0))

        if btn_chsn(mx, my, click, draw_button, draw_text1, glare_draw):
            return draw()
        if btn_chsn(mx, my, click, opt_button, opt_text, glare_opt):
            return draw()
        if btn_chsn(mx, my, click, abt_button, abt_text, glare_abt):
            return draw()
        click = False
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("YES")
                click = True
        pygame.display.update()
        clock.tick(FPS)


def draw():
    game_window.fill(WHITE)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return main_menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(FPS)

# def opt():

# def abt():


if __name__ == '__main__':
    main_menu()
