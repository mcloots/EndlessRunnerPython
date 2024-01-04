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

# Zombie
zombie = Actor('walk1')
zombie.x = 100
zombie.y = 470
zombie.images = []
for i in range(1, 11):
    zombie.images.append(f"walk{i}")
zombie.fps = 40

velocity = 0 # How fast our zombie moves in the up/down direction
gravity = 1 # Gravity will change our velocity. The bigger, the more pull towards the ground

def update():
    global velocity # Makes a global variable of velocity

    #### ZOMBIE ####
    # zombie.next_image() is also possible, this way you don't heed the animate() and the fps property
    zombie.animate()

    # Jump in the air when the up arrow is pressed
    if keyboard.up and zombie.y == 470:
        velocity = -18
    zombie.y = zombie.y + velocity
    velocity += gravity

    # Stop zombie falling of the screen
    if zombie.y > 470:
        velocity = 0
        zombie.y = 470

    #### BAT ####
    bat.animate()
    bat.x -= 3
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
    zombie.draw()

# Run the game
pgzrun.go()
