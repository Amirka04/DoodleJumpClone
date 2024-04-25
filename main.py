import pygame
from pygame.locals import *

import sys

# import my classes
from Player import Player
import settings


# initialization pygame
pygame.init()
pygame.font.init()


# screen
screen = pygame.display.set_mode(settings.WindowSize)
clock = pygame.time.Clock()

# all sprites
memSprite = pygame.sprite.Group()

# Player object
player = Player("src/Slime_Alien.png", (120, 120), (100, 100))


# добавление спрайта в список спрайтов
memSprite.add(player)



# main loop game
while settings.isRunGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunGame = False
            sys.exit()

    # update
    memSprite.update()

    screen.fill(settings.bg_color)
    # draw
    # ------
    memSprite.draw(screen)
    # ------
    clock.tick(60)
    pygame.display.flip()

pygame.quit()