# Install pgzero (Settings - Project - Interpreter)
import pgzrun
import random
from pgzhelper import *

# Game screen dimension
TITLE = 'Zombie Runner'
WIDTH = 800
HEIGHT = 600

# Colours
black = (0, 0, 0)
brown = (71, 34, 18)

# Moon
moon = Actor('moon')
moon.x = WIDTH - 100
moon.y = 80


# Rect: 0,0 = x, y
def draw():
    screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 100), (black))  # Sky
    screen.draw.filled_rect(Rect(0, 500, WIDTH, HEIGHT), (brown))  # Ground

    moon.draw()


# Run the game
pgzrun.go()
