# Install pgzero (Settings - Project - Interpreter)
import pgzrun
import random
from pgzhelper import *

# Game screen dimension
TITLE = 'Zombie Runner'
WIDTH = 800
HEIGHT = 600

music.play('music')

# Colours
black = (0, 0, 0)
brown = (71, 34, 18)
red = (212, 47, 47)
white = (255, 255, 255)

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

# Gost
ghost = Actor('ghost')
ghost.x = random.randint(900, 5000)
ghost.y = random.randint(250, 350)
ghost.scale = 0.05

# Obstacles
obstacles = [] # Empty list that will hold the spike obtacles
obstacles_timeout = 0 # This number is a counter to ensure sikes appear in our game - but not all at once



# Game variables
score = 0
game_over = False
deathsound = False

def update():
    global velocity # Makes a global variable of velocity
    global score
    global obstacles_timeout
    global game_over
    global deathsound

    if keyboard.down:
        game_over = False
        score = 0

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

    #### GHOST ####
    if not game_over:
        ghost.x -= 5
        if ghost.x < -50:
            ghost.x = random.randint(900, 5000)
            ghost.y = random.randint(250, 350)

    # Zombie & Ghost collision
    if zombie.colliderect(ghost):
        sounds.collect.play()
        ghost.x = random.randint(900, 5000)
        ghost.y = random.randint(250, 350)
        score += 5

    #### SPIKES ####
    if not game_over:
        obstacles_timeout += 1 # On each frame refresh we add 1 to the counter
        if obstacles_timeout > random.randint(60, 7000):
            spikes = Actor('spikes')
            spikes.x = 860
            spikes.y = 500
            spikes.scale = 0.25
            obstacles.append(spikes) # Add spikes to list
            obstacles_timeout = 0

        # Move spikes across the screen
        for spikes in obstacles:
            spikes.x -= 8
            if spikes.x < -50:
                obstacles.remove(spikes)
                score += 1

        # Collision between zombie and spikes
        if zombie.collidelist(obstacles) != -1: # -1 is no collision
            game_over = True
            obstacles.remove(spikes)
            if not deathsound:
                sounds.gameover.play()
            deathsound = True


# Rect: 0,0 = x, y
def draw():
    screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT - 100), (black))  # Sky
    screen.draw.filled_rect(Rect(0, 500, WIDTH, HEIGHT), (brown))  # Ground
    # screen.draw.text('Score: ' + str(score), color = (red), fontname = 'creepster', fontsize = 30)

    if game_over:
        screen.draw.text('Game Over', centerx=380, centery=150, color=(red), fontname = 'creepster', fontsize = 80)
        screen.draw.text(f"Score: {score}", centerx=380, centery=300, color=(white), fontname='creepster', fontsize=60)
        music.stop()
    else:
        screen.draw.text(f"Score: {score}", (20, 20), color=(red), fontname='creepster', fontsize=30)
        moon.draw()
        houses.draw()
        bat.draw()
        zombie.draw()
        ghost.draw()

        for spikes in obstacles:
            spikes.draw()
# Run the game
pgzrun.go()
