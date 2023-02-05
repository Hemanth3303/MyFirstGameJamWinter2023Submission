import pygame
import sys
from random import randint

from config import *
from states import *
from player import *
from block import *

class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.display.set_caption("My First Game Jam Winter 2023 Submission")
        self.screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
        self.clock=pygame.time.Clock()
        self.font=pygame.font.Font("./res/fonts/consola.ttf", 24)
        self.state=State.MENU
        self.player=Player((SCREEN_WIDTH/2, SCREEN_HEIGHT-100), (20, 20))
        self.blocks=[]
        self.pipe_timer=0
        self.score=0

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
        if keys[pygame.K_SPACE] and self.state==State.MENU:
            self.state=State.PLAYING
        if keys[pygame.K_r] and self.state==State.GAMEOVER:
            self.restart()
            self.state=State.PLAYING

        # player movement
        if keys[pygame.K_a]:
            self.player.vel.x=-PLAYER_SPEED
        elif keys[pygame.K_d]:
            self.player.vel.x=PLAYER_SPEED

    def update(self):
        self.dt=(self.clock.tick(TARGET_FPS)/1000)
        self.fps=self.clock.get_fps()

        match self.state:
            case State.MENU:
                pass
            case State.PLAYING:
                self.pipe_timer+=self.dt
                if self.pipe_timer>0.5:
                    self.spawn_pipes()
                    self.pipe_timer=0
                self.player.update(self.dt)
                for pipe in self.blocks:
                    pipe.update(self.dt)
                    if pygame.sprite.collide_rect(pipe, self.player):
                        self.state=State.GAMEOVER
                    if pipe.rect.y>SCREEN_HEIGHT:
                        self.blocks.remove(pipe)
                        self.score+=1
                # print(f"no of blocks={len(self.blocks)}")
            case State.GAMEOVER:
                pass
            case State.EXIT:
                self.running=False

    def render(self):
        self.screen.fill(BLACK)

        match self.state:
            case State.MENU:
                self.drawText("Made Using Python And Pygame", (SCREEN_WIDTH/2, SCREEN_HEIGHT/3.7))
                self.drawText("For 'My First Game Jam Winter 2023'", (SCREEN_WIDTH/2, SCREEN_HEIGHT/3))
                self.drawText("Instructions:", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2.25))
                self.drawText("Press Space To Start", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                self.drawText("Press A To Move Left And D To Right", (SCREEN_WIDTH/2, SCREEN_HEIGHT/1.75))
                self.drawText("Avoid Falling Red Rectangles", (SCREEN_WIDTH/2, SCREEN_HEIGHT/1.5))
            case State.PLAYING:
                self.drawText("Score="+str(self.score), (50, 15))
                self.player.draw(self.screen)
                for pipe in self.blocks:
                    pipe.draw(self.screen)
            case State.GAMEOVER:
                self.drawText("Game Over", (SCREEN_WIDTH/2, SCREEN_HEIGHT/3))
                self.drawText("Final Score="+str(self.score), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2.5))
                self.drawText("Press R To Restart", (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            case State.EXIT:
                pass

        pygame.display.flip()

    def shutdown(self):
        pygame.mixer.quit()
        pygame.quit()
        sys.exit(0)

    def spawn_pipes(self):
        pipe_width=randint(20, 100)
        pipe_height=randint(20, 100)

        y=-pipe_height
        x=randint(0, SCREEN_WIDTH-pipe_width)

        self.blocks.append(Pipe((x, y), (pipe_width, pipe_height)))

    def drawText(self, text_str, pos):
        text=self.font.render(text_str, True, WHITE, BLACK)
        textRect=text.get_rect()
        textRect.center=pos
        self.screen.blit(text, textRect)

    def restart(self):
        self.player=Player((SCREEN_WIDTH/2, SCREEN_HEIGHT-100), (20, 20))
        self.score=0
        self.blocks=[]