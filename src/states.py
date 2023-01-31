from enum import Enum

class State(Enum):
    MENU=0,
    PLAYING=1,
    PAUSE=2,
    OPTIONS=3,
    GAMEOVER=4,
    EXIT=5,