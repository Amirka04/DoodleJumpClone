import pygame

# global variable in game
WindowSize = [600, 800] # размер окна
WindowCenter = int(WindowSize[0] / 2), int(WindowSize[1] / 2)
bg_color = (150, 150, 150) # фоновый цвет
isRunGame = True    # переменная контролирующая основной цикл
gameState = "menu"  # переменая отвечает на состояние игры (меню же игра)
clock = pygame.time.Clock() # класс времени в игре
fontGame = None     # шрифт игры
score = 0
platformHeightGeneration = 70