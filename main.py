import pygame
import math
import random
from pygame import mixer

# Initialize the pygame
pygame.init()
# to create the screen, here 600=height
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('123.jpeg')

#background sound
#mixer.music.load()
#mixer.music.play(-1)

# title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('planet.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('space.png')
PlayerX = 370
PlayerY = 480
PlayerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(5)
    enemyY_change.append(10)

# bullet
# read= you cant see the bullet on the screen
# fire=the bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
score = 0

score_value = 0
font = pygame.font.Font('freesansbold.ttf',50)

textX = 10
testY = 10

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True,(255, 182, 193))
    screen.blit(score,(x,y))

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 15, y + 3))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# ctrl+alt+l = code systematic hojata hai

# game loop

running = True
while running:

    # RGB=red green blue
    screen.fill((230, 230, 250))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check wheather its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                PlayerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # get the current x coordinate of the spaceship
                    bulletX = PlayerX
                    fire_bullet(bulletX, bulletY)
                    bulletY_change = 0.8

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0

    PlayerX += PlayerX_change

    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736
    # checking for boundaries of spaceship so it doesnt go out of bounds

    # enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]
            # collision

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(PlayerX,PlayerY)
    show_score(textX,testY)
    pygame.display.update()
