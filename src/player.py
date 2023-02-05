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

        # drag effect
        if self.vel.x!=0 and self.vel.x>1:
            self.vel.x-=PLAYER_DRAG*PLAYER_SPEED
        if self.vel.x!=0 and self.vel.x<1:
            self.vel.x+=PLAYER_DRAG*PLAYER_SPEED

        if self.rect.x < 0:
            self.rect.x=0
        if self.rect.x+self.rect.width > SCREEN_WIDTH:
            self.rect.x=SCREEN_WIDTH-self.rect.width

    def draw(self, target_surface):
        target_surface.blit(self.sprite, self.rect)