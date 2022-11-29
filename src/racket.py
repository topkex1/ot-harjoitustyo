import pygame


class Racket(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.moves = False
