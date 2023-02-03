import pygame
from config import *

class Pipe:
    def __init__(self, pos, size):
        self.sprite=pygame.Surface(size)
        self.sprite.fill(RED)
        self.rect=pygame.Rect(pos, size)

        self.vel=pygame.Vector2(1, 0)

    def update(self, dt):
        self.rect.topleft-=self.vel*PIPE_SPEED*dt

    def draw(self, target_surface):
        target_surface.blit(self.sprite, self.rect)