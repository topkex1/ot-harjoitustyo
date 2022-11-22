import pygame

class Level():
	#def __init__(self,x1,x2,y1,y2):
	def __init__(self,ball,racket,x1,x2,y1,y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.center = (x2//2),(y2//2)
		self.p1_center = x1,y2//2
		self.p2_center = x2, y2//2
		self.player1 = racket(20,100,self.p1_center[0],self.p1_center[1])
		self.player2 = racket(20,100,self.p2_center[0]-20,self.p2_center[1])

		self.players = pygame.sprite.Group()
		self.all = pygame.sprite.Group()

		self.players.add(self.player1,self.player2)
		self.all.add(self.player1,self.player2,ball(20,self.center[0],self.center[1]))

	def move_player(self,player):
		player.moves = True
		


