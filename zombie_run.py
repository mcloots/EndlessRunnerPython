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

# Haunted houses
houses = Actor('houses')
houses.x = WIDTH / 2
houses.y = HEIGHT / 2

# Bat
bat = Actor('bat1')
bat.scale = 0.5
bat.x = 900
bat.y = 100
bat.images = ['bat1', 'bat2', 'bat3', 'bat4']
bat.fps = 10

def update():
    #### BAT ####
    bat.animate()
    bat.x = bat.x - 3
    if bat.x < -50:
        bat.x = random.randint(1000,15000)
        bat.y = random.randint(100, 250)

# Rect: 0,0 = x, y
def draw():
    screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 100), (black))  # Sky
    screen.draw.filled_rect(Rect(0, 500, WIDTH, HEIGHT), (brown))  # Ground

    moon.draw()
    houses.draw()
    bat.draw()

# Run the game
pgzrun.go()
