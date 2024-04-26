import pygame

import settings


class Object(pygame.sprite.Sprite):
    def __init__(self, texture, position, size):
        super().__init__()
        self.image = pygame.image.load(texture)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = position