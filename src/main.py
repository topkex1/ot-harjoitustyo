import pygame

from ball import Ball
from racket import Racket
from level import Level
from render import Render
from events import Events



def main():
	window_width = 1280
	window_height = 720

	window = pygame.display.set_mode((window_width, window_height))
	pygame.init()

	level = Level(Ball,Racket,0,1280,0,720)
	render = Render(level,window,60)
	events = Events()
	

	while True:
		events.check_events()
		render.draw()

if __name__ == "__main__":
	main()