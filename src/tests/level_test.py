import unittest
from ball import Ball
from racket import Racket
from level import Level

class TestLevel(unittest.TestCase):
	def setUp(self):
		self.level = Level(Ball, Racket, 0, 1280, 0, 720)

	def test_player1_can_move_up(self):
		y_pos = self.level.player1.y
		self.level.player1.moves = -1
		self.level.move_player(self.level.player1)
		self.assertGreater(y_pos, self.level.player1.y)

	def test_player1_can_move_down(self):
		y_pos = self.level.player1.y
		self.level.player1.moves = 1
		self.level.move_player(self.level.player1)
		self.assertLess(y_pos,self.level.player1.y)
		


	#def test_player1_bounds(self):
	#	self.level.player1.moves = 1
	#	while self.level.player1.moves != 0:
	#		self.level.move_player(self.level.player1)

