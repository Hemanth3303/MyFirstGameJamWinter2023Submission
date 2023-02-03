import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image=pygame.image.load("res/sprites/blob.png").convert_alpha()
        self.rect=self.image.get_rect(topleft=pos)

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