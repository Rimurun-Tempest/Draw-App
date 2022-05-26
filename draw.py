import pygame
import sys
from button_class import Button
import webbrowser
import numpy

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (19, 69, 99)
YELLOW = (255,255,0)
GREY = (211, 211, 211)
clock = pygame.time.Clock()
FPS = 120

game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Assets
sysfont = pygame.font.SysFont(None, 60)
background = pygame.image.load('Assets/bg.png').convert()
title = pygame.image.load("Assets/Title.png").convert_alpha()
icon = pygame.image.load('Assets/draw.png').convert()
options_page = pygame.image.load('Assets/options.png').convert()
about_page = pygame.image.load('Assets/about.png').convert()

# Initializing
just_background = pygame.image.load('Assets/bg.png').convert()
background.blit(title, (140, 50))
pygame.display.set_icon(icon)
pygame.display.set_caption("Draw V2")


def main_menu():

    game_window.blit(background, (0, 0))
    BUTTON_X = 220
    BUTTON_Y = 170
    BUTTON_SPACE = 60
    # Draw Button
    draw_button = Button(BUTTON_X, BUTTON_Y, game_window)
    draw_button.draw_text('Draw', sysfont, CYAN)

    # Options Button
    options_button = Button(BUTTON_X, BUTTON_Y+BUTTON_SPACE, game_window)
    options_button.draw_text('Options', sysfont, CYAN)

    # About Button
    about_button = Button(BUTTON_X, BUTTON_Y+2*BUTTON_SPACE, game_window)
    about_button.draw_text('About', sysfont, CYAN)

    click = False
    pygame.display.update()

    while True:

        # Mouse Positon
        mx, my = pygame.mouse.get_pos()
        game_window.blit(background, (0, 0))

        if draw_button.button_selected(mx, my, click):
            return draw()
        if options_button.button_selected(mx, my, click):
            return options()
        if about_button.button_selected(mx, my, click):
            return about()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
        pygame.display.update()
        clock.tick(FPS)

class Draw:
    prev_point = None
    def __init__(self, surface):
        self.drawsurface = surface
        
    def draw(self, color, pos):
            if self.prev_point is not None:
                pygame.draw.aaline(self.drawsurface, color, self.prev_point,pos,1) 
            self.prev_point = pos

    def update(self, surface):
        surface.blit(self.drawsurface,(0,0)) 

    def erase(self,pos):
        pygame.draw.circle(self.drawsurface,BLACK,pos, 10, 0)

    def clear(self):
        self.drawsurface.fill(WHITE)
    # def fill color

    def fill(self, position, fill_color):
        surface = self.drawsurface
        fill_color = surface.map_rgb(fill_color)  # Convert the color to mapped integer value.
        surf_array = pygame.surfarray.pixels2d(surface)  # Create an array from the surface.
        current_color = surf_array[position]  # Get the mapped integer color value.

        # 'frontier' is a list where we put the pixels that's we haven't checked. Imagine that we first check one pixel and 
        # then expand like rings on the water. 'frontier' are the pixels on the edge of the pool of pixels we have checked.
        #
        # During each loop we get the position of a pixel. If that pixel contains the same color as the ones we've checked
        # we paint it with our 'fill_color' and put all its neighbours into the 'frontier' list. If not, we check the next
        # one in our list, until it's empty.

        frontier = [position]
        while len(frontier) > 0:
            x, y = frontier.pop()
            try:  # Add a try-except block in case the position is outside the surface.
                if surf_array[x, y] != current_color:
                    continue
            except IndexError:
                continue
            surf_array[x, y] = fill_color
            # Then we append the neighbours of the pixel in the current position to our 'frontier' list.
            frontier.append((x + 1, y))  # Right.
            frontier.append((x - 1, y))  # Left.
            frontier.append((x, y + 1))  # Down.
            frontier.append((x, y - 1))  # Up.

        pygame.surfarray.blit_array(surface, surf_array)

    def isvalid(self, x, y):
        if x<0 or x>900 or y<0 or y>500:
            return False 
        return True
    def image(self):
        return self.drawsurface


def draw():

    game_window.fill(GREY)
    TOOLS_Y = 100
    ds= pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT-TOOLS_Y))
    ds.fill(WHITE)
    draw_surface = Draw(ds)

    ############# Loading Assets ####################
    save_icon = pygame.image.load('Assets/save_icon.png').convert_alpha()
    save_icon = pygame.transform.scale(save_icon,(98,98))
    save_button = Button(0,500,game_window)
    save_button.draw_button(BLACK,100,100,save_icon)

    bucket_icon = pygame.image.load('Assets/bucket.png').convert_alpha()
    bucket_icon = pygame.transform.scale(bucket_icon,(98,98))
    bucket_button = Button(300,500,game_window)
    bucket_button.draw_button(BLACK,100,100,bucket_icon)

    paint_icon = pygame.image.load('Assets/paint.png').convert_alpha()
    paint_icon = pygame.transform.scale(paint_icon,(98,98))
    paint_button = Button(400, 500, game_window)
    paint_button.draw_button(BLACK,100,100,paint_icon)

    erase_icon = pygame.image.load('Assets/erase.png').convert_alpha() 
    erase_icon = pygame.transform.scale(erase_icon,(98,98))
    erase_button = Button(520,500, game_window)
    erase_button.draw_button(BLACK, 100, 100, erase_icon)


    red_color = Button(110, 508, game_window)
    red_color.draw_button(RED, 40, 40)

    green_color = Button(110,550, game_window)
    green_color.draw_button(GREEN, 40, 40)

    blue_color = Button(152, 508, game_window)
    blue_color.draw_button(BLUE, 40, 40)

    yellow_color = Button(152, 550, game_window)
    yellow_color.draw_button(YELLOW, 40, 40)

    black_color = Button(194, 508 , game_window)
    black_color.draw_button(BLACK, 40,40)

    white_color = Button(194, 550 , game_window)
    white_color.draw_button(WHITE, 40,40)
    ##################################################

    color = BLACK
    click = False
    
    mouse_mode = 0
    paint_mode = 0
    while True:
        
        mx, my = pygame.mouse.get_pos()
        
        game_window.fill(GREY)
        if red_color.button_selected(mx, my, click): 
            color = RED
        if green_color.button_selected(mx, my, click): 
            color = GREEN
        if blue_color.button_selected(mx, my, click): 
            color = BLUE
        if yellow_color.button_selected(mx, my, click): 
            color = YELLOW
        if black_color.button_selected(mx,my,click):
            color = BLACK
        if white_color.button_selected(mx,my,click):
            color = WHITE
        if save_button.button_selected(mx, my, click): 
            pygame.image.save(draw_surface.image(),'Save/test.png')  
        if bucket_button.button_selected(mx,my,click):
            paint_mode = 1
        if paint_button.button_selected(mx,my,click):
            paint_mode = 0
        if erase_button.button_selected(mx,my,click):
            draw_surface.clear()

        click = False
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return main_menu()
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
                mouse_mode = 1
                if paint_mode == 1 and draw_surface.isvalid(mx,my):
                    draw_surface.fill((mx,my),color)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                click = True
                mouse_mode = 2

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_mode = 0
                draw_surface.prev_point = None

            if event.type == pygame.MOUSEMOTION and mouse_mode == 2 and paint_mode == 0:
                draw_surface.erase((mx,my))

            if event.type == pygame.MOUSEMOTION and mouse_mode == 1 and paint_mode == 0:
                draw_surface.draw(color,(mx,my))   
        
        draw_surface.update(game_window)
        pygame.display.update()
        clock.tick(FPS)



def options():
    game_window.blit(options_page,(0,0))
    
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


def about():

    game_window.blit(about_page,(0,0))
    github = pygame.image.load('Assets/git.png').convert_alpha()
    github = pygame.transform.scale(github,(300,100))

    git_button = Button(200,400,game_window)
    git_button.draw_button(BLACK,100,100,github)

    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        game_window.blit(about_page, (0, 0))

        if git_button.button_selected(mx, my, click): 
            webbrowser.open('https://github.com/Rimurun-Tempest/Draw-App')
        click = False        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return main_menu()
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(FPS)    
if __name__ == '__main__':
    main_menu()
