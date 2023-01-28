import pygame
import sys
import config

class Game:
    def __init__(self):
        print("__init__")
        
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.display.set_caption("My First Game Jam Winter 2023 Submission")
        self.screen=pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.DOUBLEBUF)
        self.clock=pygame.time.Clock()

        self.dt=0
        self.fps=0
        self.running=True

    def handle_events(self):
        print("handle events")

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    self.running=False

    def update(self):
        print("update")

        self.dt=self.clock.tick(config.TARGET_FPS)
        self.fps=self.clock.get_fps()

    def render(self):
        print("render")

        pygame.display.flip()

    def shutdown(self):
        print("shutdown")

        pygame.mixer.quit()
        pygame.quit()
        sys.exit(0)