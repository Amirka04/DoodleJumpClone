import pygame
from pygame.locals import *

import sys

# import my classes
from Object import Object
import settings


# initialization pygame
pygame.init()
pygame.font.init()


# screen
screen = pygame.display.set_mode(settings.WindowSize)
pygame.display.set_caption("Doodle Jump python clone")
pygame.display.set_icon(pygame.image.load("src/Icon.png"))

clock = pygame.time.Clock()

# all sprites
memSprite = pygame.sprite.Group()

# Player object
player = Object("src/lik-left.png", (settings.WindowSize[0] / 2, settings.WindowSize[1] / 2), (80, 80))


infinityBackground = [
                        Object("src/bck.png", (settings.WindowSize[0] / 2, settings.WindowSize[1] / 2), (settings.WindowSize[0], settings.WindowSize[1])),
                        Object("src/bck.png", (settings.WindowSize[0] / 2, settings.WindowSize[1] / 2 + settings.WindowSize[1]), (settings.WindowSize[0], settings.WindowSize[1]))
                    ]




# добавление спрайта в список спрайтов
memSprite.add(infinityBackground)
memSprite.add(player)





# main loop game
while settings.isRunGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunGame = False
            sys.exit()

    # update
    memSprite.update()

    keyPressed = pygame.key.get_pressed()
    

    screen.fill(settings.bg_color)
    
    # draw
    # ------

    memSprite.draw(screen)
    
    # ------
    
    clock.tick(60)
    pygame.display.flip()

pygame.quit()