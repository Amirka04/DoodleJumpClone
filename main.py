import pygame
from pygame.locals import *
from random import randrange

import sys

# import my classes
from Object import Object
import settings


# functions
def scrollBackGround(infinityBackground : list[Object], speed):
    for i in range(0, len(infinityBackground)):
        if infinityBackground[i].rect.y > settings.WindowSize[1] * 2:
            infinityBackground[i].rect.y = 1 - infinityBackground[i].rect.h
        infinityBackground[i].rect.y += speed



def centeredObject(object1_in : list|tuple, object2_to : list|tuple):
    return (object1_in[0] - object2_to[0] / 2, object1_in[1] - object2_to[1] / 2)



def setScore(font, text, score):
    return font.render(text + str(score), 1, (50, 50, 50))



def generatePlatform(platforms : list[Object], example : Object):
    ex = Object( 
        example.srcImage,
        (randrange(int(0 + example.rect.width / 2), settings.WindowSize[0] - example.rect.height), platforms[-1].rect.y - 60),
        example.rect.size
    )

    platforms.append(ex)
    


def GetCollisionPlatform(platforms : list[Object], player : Object, velocity : int):
    if velocity > 0:
        for i in platforms:
            if player.rect.colliderect(i.rect) and (player.rect.y + player.rect.height / 2.0 < i.rect.y - i.rect.height / 2.0):
                return i
    return None



# initialization pygame
pygame.init()
pygame.font.init()


# screen
screen = pygame.display.set_mode(settings.WindowSize)
pygame.display.set_caption("Doodle Jump python clone")
pygame.display.set_icon(pygame.image.load("src/Icon.png"))



# Player object
player = Object("src/lik-left.png", settings.WindowCenter, (70, 70))
DefPowerJump = PowerJump = -15
iSJumpVisible = True
player.rect.x -= player.rect.size[0] / 2
player.rect.y += 100



infinityBackground = [
                        Object("src/bck.png", (0, 0 + settings.WindowSize[1]), pygame.Vector2(settings.WindowSize)),
                        Object("src/bck.png", (0, 0 - settings.WindowSize[1]), pygame.Vector2(settings.WindowSize)),
                        Object("src/bck.png", (0, 0), pygame.Vector2(settings.WindowSize))
                    ]


platformObject = Object("src/platform.png", settings.WindowCenter, (80, 15))
lastPlatform = None
isPlatformScroll = False
cntPlatform = 15

platformObject.rect.x = player.rect.x
platformObject.rect.y = player.rect.y + player.rect.height + 40

platforms = []
platforms.append(platformObject)


for i in range(0, 15):
    generatePlatform(platforms, platformObject)


settings.fontGame = pygame.font.Font("src/ComicSans.ttf", 35)

scoreLabel = settings.fontGame.render("Score: " + str(settings.score), 1, (50, 50, 50))
startLabel = settings.fontGame.render("Press to Start", 1, (50, 50, 50))


# main loop game
while settings.isRunGame:
    dt = settings.clock.get_fps() / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunGame = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if settings.gameState == "menu":
                settings.gameState = "game"
                settings.score = 0
                
                player.rect.x, player.rect.y = settings.WindowCenter
                platformObject.rect.x, platformObject.rect.y = settings.WindowCenter
                PowerJump = -10
                platforms.clear()
                platforms.append(platformObject)
                for i in range(0, 15):
                    generatePlatform(platforms, platformObject)

                infinityBackground = [
                        Object("src/bck.png", (0, 0 + settings.WindowSize[1]), pygame.Vector2(settings.WindowSize)),
                        Object("src/bck.png", (0, 0 - settings.WindowSize[1]), pygame.Vector2(settings.WindowSize)),
                        Object("src/bck.png", (0, 0), pygame.Vector2(settings.WindowSize))
                ]

    
    # получение состояния нажатий мыши и клавиши
    keyPressed = pygame.key.get_pressed()
    mouseButtonPressed = pygame.mouse.get_pressed()


    screen.fill(settings.bg_color)
    

    # draw
    # ------

    # Режим меню
    if settings.gameState == "menu":
        for bg in infinityBackground:
            bg.render(screen)
        scrollBackGround(infinityBackground, 3)
        screen.blit(startLabel, centeredObject(settings.WindowCenter, startLabel.get_size()))
        

    # Режим игры
    elif settings.gameState == "game":
        infinityBackground[-1].render(screen)

        for platform in platforms:
            if platform.rect.y - platform.rect.h > settings.WindowSize[1]:
                del platforms[ platforms.index(platform) ]
                generatePlatform(platforms, platformObject)
            platform.render(screen)

        player.render(screen)

        screen.blit(setScore(settings.fontGame, "Score: ",int(settings.score)), (0, 0))
        
        platformMoved = GetCollisionPlatform(platforms, player, PowerJump)
        
        if platformMoved:
            PowerJump = DefPowerJump
            settings.score += 1 if lastPlatform != platformMoved else 0
            lastPlatform = platformMoved
        

        PowerJump += 0.5
        player.rect.y += PowerJump if player.rect.y + PowerJump > settings.WindowCenter[1] / 2 else 0
        
        if lastPlatform:
            deltaScroll = -PowerJump if lastPlatform.rect.y < int(settings.WindowCenter[1] * 1.5) and PowerJump < 0 else 0
            for index in range(0, len(platforms)):
                platforms[index].rect.y += deltaScroll

        if player.rect.y + player.rect.h > settings.WindowSize[1]:
            settings.gameState = "menu"

        # move player
        if keyPressed[pygame.K_d] or keyPressed[pygame.K_RIGHT]:
            player.rect.x += 10 if player.rect.x - player.rect.w / 2 < settings.WindowSize[0] else 0

        if keyPressed[pygame.K_a] or keyPressed[pygame.K_LEFT]:
            player.rect.x -= 10 if player.rect.x + player.rect.w / 2 > 0 else 0


    # ------
    
    settings.clock.tick(60)
    pygame.display.flip()


pygame.quit()