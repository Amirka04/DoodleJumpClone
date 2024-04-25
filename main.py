import pygame
from pygame.locals import *


import sys


# initialization pygame
pygame.init()
pygame.font.init()



# global variable in game
WindowSize = (1024, 640)
bg_color = (150, 150, 150)
isRunGame = True


# screen
screen = pygame.display.set_mode(WindowSize)

# main loop game
while isRunGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunGame = False
            sys.exit()

    screen.fill(bg_color)

    # draw
    # ------
    


    # ------
    pygame.display.flip()