import pygame

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ship_icon.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('airplane.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))


running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()