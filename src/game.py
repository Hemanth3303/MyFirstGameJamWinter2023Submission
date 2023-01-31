import pygame
import sys
from config import *
from states import *

class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.display.set_caption("My First Game Jam Winter 2023 Submission")
        self.screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
        self.clock=pygame.time.Clock()
        self.state=State.PLAYING

        self.player=pygame.image.load("src/res/sprites/blob.png").convert_alpha()
        self.playerRect=self.player.get_rect()
        self.playerRect.x=300
        self.playerRect.y=200

        self.dx=0
        self.dy=0

        self.dt=0
        self.fps=0
        self.running=True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.state=State.EXIT

        keys=pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_ESCAPE]:
                self.state=State.EXIT

            if keys[pygame.K_a]:
                self.dx=-PLAYER_SPEED
            if keys[pygame.K_d]:
                self.dx=PLAYER_SPEED
            if keys[pygame.K_w]:
                self.dy=-PLAYER_SPEED
            if keys[pygame.K_s]:
                self.dy=PLAYER_SPEED

    def update(self):
        if self.state==State.EXIT:
            self.running=False

        self.dt=self.clock.tick(TARGET_FPS)
        self.fps=self.clock.get_fps()

        self.playerRect.x+=(self.dx*self.dt)
        self.playerRect.y+=(self.dy*self.dt)

    def render(self):
        self.screen.blit(self.player, self.playerRect)
        pygame.display.update()

    def shutdown(self):
        pygame.mixer.quit()
        pygame.quit()
        sys.exit(0)