import pygame

import settings


class Object:
    def __init__(self, texture, position, size):
        self.image = pygame.image.load(texture)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        # self.rect.center = settings.WindowCenter
        self.rect.x, self.rect.y = position
        self.srcImage = texture

        
    def render(self, screen : pygame.Surface):
        screen.blit(self.image, self.rect)
