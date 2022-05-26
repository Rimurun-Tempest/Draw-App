import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (19, 69, 99)

class Button:
    alpha_value = 40
    selected_color = BLACK

    # Constructor to
    def __init__(self, x, y, surface) -> None:
        self.x = x
        self.y = y
        self.surface = surface

    # Writing text in the button
    def draw_text(self, text, font, color) -> None:
        self.text = text
        self.color = color
        self.font = font
        self.textobj = self.font.render(self.text, True, self.color)
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (self.x, self.y)

        self.glare = pygame.Surface(self.textobj.get_size())
        self.glare.set_alpha(self.alpha_value)
        self.glare.fill(self.selected_color)

    def draw_button(self, color, height, width, surface = None ):
        self.color = color
        self.textobj = pygame.Surface((width, height))
        self.textobj.fill(color)
        if surface is not None:
            self.textobj = surface
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (self.x,self.y)

        self.glare = pygame.Surface(self.textobj.get_size())
        self.glare.set_alpha(self.alpha_value)
        self.glare.fill(self.selected_color)

    # Rendering the button surface
    def button_selected(self, mx, my, click) -> bool:
        if self.textrect.collidepoint(mx, my):
            self.surface.blit(self.textobj, self.textrect)
            self.surface.blit(self.glare, self.textrect)
            if click:
                return True
        elif ~self.textrect.collidepoint(mx, my):
            self.surface.blit(self.textobj, self.textrect)
        return False