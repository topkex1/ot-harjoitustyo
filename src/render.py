import pygame


class Render:
    def __init__(self, level, display, tick):
        self.tickrate = tick
        self.clock = pygame.time.Clock()
        self.level = level
        self.display = display

    def draw(self):
        self.display.fill(0)
        for i in self.level.all:
            self.display.blit(i.image, (i.x, i.y))
        self.clock.tick(self.tickrate)
        pygame.display.flip()
