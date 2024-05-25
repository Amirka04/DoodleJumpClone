import pygame
import Parser

# global variable in game
global_setting = Parser.Settings()

WindowSize = pygame.Vector2( global_setting.getWindowData("size") )
WindowSize = list(map(int, WindowSize))
WindowCenter = int(WindowSize[0] / 2), int(WindowSize[1] / 2)
bg_color = (150, 150, 150) # фоновый цвет
isRunGame = True    # переменная контролирующая основной цикл
gameState = "menu"  # переменая отвечает на состояние игры (меню же игра)
clock = pygame.time.Clock() # класс времени в игре
fontGame = None     # шрифт игры
score = 0
platformHeightGeneration = 70