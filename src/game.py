import pygame
import sys
from random import randint

from config import *
from states import *
from player import *
from pipe import *

class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.display.set_caption("My First Game Jam Winter 2023 Submission")
        self.screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
        self.clock=pygame.time.Clock()
        self.state=State.PLAYING
        self.player=Player((SCREEN_WIDTH/2, SCREEN_HEIGHT-100), (20, 20))
        self.pipes=[]
        self.pipe_timer=0

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

        # player movement
        if keys[pygame.K_a]:
            self.player.vel.x=-PLAYER_SPEED
        elif keys[pygame.K_d]:
            self.player.vel.x=PLAYER_SPEED

    def update(self):
        if self.state==State.EXIT:
            self.running=False

        self.dt=(self.clock.tick(TARGET_FPS)/1000)
        self.fps=self.clock.get_fps()

        self.pipe_timer+=self.dt

        if self.pipe_timer>0.5:
            self.spawn_pipes()
            self.pipe_timer=0

        if self.state==State.PLAYING:
            self.player.update(self.dt)
            for pipe in self.pipes:
                pipe.update(self.dt)
                if pygame.sprite.collide_rect(pipe, self.player):
                    self.state=State.GAMEOVER
                if pipe.rect.y>SCREEN_HEIGHT:
                    self.pipes.remove(pipe)
        # print(f"no of pipes={len(self.pipes)}")

    def render(self):
        self.screen.fill((0, 0, 0))

        if self.state==State.PLAYING:
            self.player.draw(self.screen)
            for pipe in self.pipes:
                pipe.draw(self.screen)

        pygame.display.flip()

    def shutdown(self):
        pygame.mixer.quit()
        pygame.quit()
        sys.exit(0)

    def spawn_pipes(self):
        pipe_width=randint(50, 50)
        pipe_height=randint(50, 50)

        y=-pipe_height
        x=randint(0, SCREEN_WIDTH-pipe_width)

        self.pipes.append(Pipe((x, y), (pipe_width, pipe_height)))