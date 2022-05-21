import pygame
import sys


WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (19, 69, 99)

clock = pygame.time.Clock()
FPS = 60

game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
icon = pygame.image.load('Assets/draw.png').convert()
pygame.display.set_caption("Draw V2")
pygame.display.set_icon(icon)

# Assets
sysfont = pygame.font.SysFont(None, 60)
background = pygame.image.load('Assets/background.jpg').convert()
title = pygame.image.load("Assets/Title.png").convert_alpha()
background.blit(title, (140, 50))


class Button:
    alpha_value = 40
    selected_color = BLACK

    # Constructor to  
    def __init__(self, x, y, surface)->None:
        self.x = x
        self.y = y
        self.surface = surface

    # Writing text in the button
    def draw_text(self, text, font, color)->None:
        self.text = text
        self.color = color
        self.font = font
        self.textobj = self.font.render(self.text, True, self.color)
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (self.x, self.y)

        self.glare = pygame.Surface(self.textobj.get_size())
        self.glare.set_alpha(self.alpha_value)
        self.glare.fill(self.selected_color)

    # Rendering the button surface
    def button_selected(self, mx, my, click)->bool:
        if self.textrect.collidepoint(mx, my):
            game_window.blit(self.textobj, self.textrect)
            game_window.blit(self.glare, self.textrect)
            if click:
                return True
        elif ~self.textrect.collidepoint(mx, my):
            game_window.blit(self.textobj, self.textrect)
        return False        


# Drawing Text on Screen
def draw_text(text, font, surface, color, x, y):
    textobj = font.render(text, True, color)
    # textobj.set_colorkey(WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    game_window.blit(textobj, textrect)
    return textobj, textrect

# Creating a Surface for chosen button


def chsn(surface, alpha=40, color=BLACK):
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

    game_window.blit(background, (0, 0))
    BUTTON_X = 220
    BUTTON_Y = 170
    BUTTON_SPACE = 60
    # Draw Button
    draw_button = Button(BUTTON_X,BUTTON_Y,game_window)
    draw_button.draw_text('Draw',sysfont,CYAN)

    # draw_text1, draw_button = draw_text('Draw', sysfont,
    #                                     game_window, CYAN, BUTTON_X, 170)

    # Options Button
    options_button = Button(BUTTON_X,BUTTON_Y+BUTTON_SPACE,game_window)
    options_button.draw_text('Options',sysfont,CYAN)
    
    # opt_text, opt_button = draw_text('Options', sysfont,
    #                                  game_window, CYAN, BUTTON_X, 230)

    # About Button
    about_button = Button(BUTTON_X,BUTTON_Y+2*BUTTON_SPACE,game_window)
    about_button.draw_text('About',sysfont,CYAN)

    # abt_text, abt_button = draw_text('About', sysfont,
    #                                  game_window, CYAN, BUTTON_X, 290)

    click = False
    pygame.display.update()

    # glare_draw = chsn(draw_text1)
    # glare_opt = chsn(opt_text)
    # glare_abt = chsn(abt_text)

    while True:

        # Mouse Positon
        mx, my = pygame.mouse.get_pos()
        game_window.blit(background, (0, 0))

        if draw_button.button_selected(mx, my, click):
            return draw()
        if options_button.button_selected(mx, my, click):
            return draw()
        if about_button.button_selected(mx, my, click):
            return draw()
        click = False
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
        pygame.display.update()
        clock.tick(FPS)


def draw():

    game_window.fill(WHITE)

    divider_vertical = pygame.draw.line(game_window, BLACK, (91, 0), (91, 480))
    divider_horizontal = pygame.draw.line(
        game_window, BLACK, (0, 389), (640, 389))
    # draw_surface = pygame.Surface((WINDOW_WIDTH-))
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
