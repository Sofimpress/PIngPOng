import pygame
from settings import *

class Paddles:

    def __init__(self, x, y, color, screen, right_key, left_key):
       self.x = x
       self.y = y
       self.color = color
       self.width = WIDTH
       self.height = HEIGHT
       self.speedy = P_SPEEDY
       self.screen = screen
       self.right_key = right_key
       self.left_key = left_key

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.right_key]:
           self.x -= self.speedy
        elif keys[self.left_key]:
            self.x += self.speedy

        if self.x <= 0:
            self.x = 0
        if self.x >= SC_WIDTH - WIDTH:
            self.x = SC_WIDTH - WIDTH

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))


    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
