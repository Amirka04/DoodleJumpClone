import pygame

import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, texture, position, size):
        super().__init__()
        self.image = pygame.image.load(texture)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = position
    

        # jump data
        self.MAX_H_JUMP = 15
        self.PowerJump = 5
        self.isJump = False
        

    def update(self):
        pass