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
        self.player=Player((100, 100), (10, 10))
        self.top_pipes=[]
        self.bottom_pipes=[]
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
        if keys[pygame.K_w]:
            self.player.vel.y=-PLAYER_SPEED
        elif keys[pygame.K_s]:
            self.player.vel.y=PLAYER_SPEED

    def update(self):
        if self.state==State.EXIT:
            self.running=False

        self.dt=(self.clock.tick(TARGET_FPS)/1000)
        self.fps=self.clock.get_fps()

        self.pipe_timer+=self.dt

        if self.pipe_timer>1:
            self.spawn_pipes()
            self.pipe_timer=0

        if self.state==State.PLAYING:
            self.player.update(self.dt)
            for top_pipe in self.top_pipes:
                top_pipe.update(self.dt)
                if top_pipe.rect.x+top_pipe.rect.width<0:
                    self.top_pipes.remove(top_pipe)
            for bottom_pipe in self.bottom_pipes:
                bottom_pipe.update(self.dt)
                if bottom_pipe.rect.x+bottom_pipe.rect.width<0:
                    self.bottom_pipes.remove(bottom_pipe)

        print(f'''TOP PIPES: {len(self.top_pipes)}, BOTTOM PIPES: {len(self.bottom_pipes)}''')

    def render(self):
        self.screen.fill((0, 0, 0))

        if self.state==State.PLAYING:
            self.player.draw(self.screen)
            for top_pipe in self.top_pipes:
                top_pipe.draw(self.screen)
            for bottom_pipe in self.bottom_pipes:
                bottom_pipe.draw(self.screen)

        pygame.display.flip()

    def shutdown(self):
        pygame.mixer.quit()
        pygame.quit()
        sys.exit(0)

    def spawn_pipes(self):
        pipe_gap=randint(30, 120)
        top_x=SCREEN_WIDTH+PIPE_WIDTH
        top_y=randint(-PIPE_HEIGHT/4, 0)
        top=Pipe((top_x, top_y), (PIPE_WIDTH, PIPE_HEIGHT))
        self.top_pipes.append(top)
        # print("spawned top")

        bottom_x=top_x
        bottom_y=top_y+pipe_gap+PIPE_HEIGHT
        PIPE_PADDING=200 # to make sure bottom pipe doesn't lift off the screen bottom
        bottom=Pipe((bottom_x, bottom_y), (PIPE_WIDTH, PIPE_HEIGHT+PIPE_PADDING))
        self.bottom_pipes.append(bottom)
        # print("spawned bottom")