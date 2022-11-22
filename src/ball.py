import pygame

class Ball(pygame.sprite.Sprite):
	def __init__(self,size,x,y):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
