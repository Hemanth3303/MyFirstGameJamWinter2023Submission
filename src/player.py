import pygame
from config import *

class Player:
    def __init__(self, pos, size):
        self.sprite=pygame.Surface(size)
        self.sprite.fill(BLUE)
        self.rect=pygame.Rect(pos, size)

        self.vel=pygame.Vector2(0, 0)

    def update(self, dt):
        self.rect.topleft+=self.vel*dt

        if self.rect.x < 0:
            self.rect.x=0
        if self.rect.x+self.rect.width > SCREEN_WIDTH:
            self.rect.x=SCREEN_WIDTH-self.rect.width
        if self.rect.y < 0:
            self.rect.y=0
        if self.rect.y+self.rect.height > SCREEN_HEIGHT:
            self.rect.y=SCREEN_HEIGHT-self.rect.height

    def draw(self, target_surface):
        target_surface.blit(self.sprite, self.rect)