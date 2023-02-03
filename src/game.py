import pygame
import sys
from config import *
from states import *
from player import *

class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.display.set_caption("My First Game Jam Winter 2023 Submission")
        self.screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
        self.clock=pygame.time.Clock()
        self.state=State.PLAYING
        self.entities=pygame.sprite.Group()

        self.player=Player(pygame.Vector2(100, 100), self.entities)

        self.dt=0
        self.fps=0
        self.running=True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.state=State.EXIT

        keys=pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.state=State.EXIT

        if keys[pygame.K_a]:
            self.player.vel.x=-PLAYER_SPEED
        elif keys[pygame.K_d]:
            self.player.vel.x=PLAYER_SPEED
        else:
            self.player.vel.x=0

        if keys[pygame.K_w]:
            self.player.vel.y=-PLAYER_SPEED
        elif keys[pygame.K_s]:
            self.player.vel.y=PLAYER_SPEED
        else:
            self.player.vel.y=0

    def update(self):
        if self.state==State.EXIT:
            self.running=False

        if self.state==State.PLAYING:
            self.entities.update(self.dt)

        self.dt=(self.clock.tick(TARGET_FPS)/1000)
        self.fps=self.clock.get_fps()

    def render(self):
        self.screen.fill((0, 0, 0))

        if self.state==State.PLAYING:
            self.entities.draw(self.screen)

        pygame.display.flip()

    def shutdown(self):
        pygame.mixer.quit()
        pygame.quit()
        sys.exit(0)