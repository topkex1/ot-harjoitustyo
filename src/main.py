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

    level = Level(Ball, Racket, 0, 1280, 0, 720)
    render = Render(level, window, 60)
    #events = Events()

    while True:
        # events.check_events()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    level.player1.moves = -1
                if event.key == pygame.K_s:
                    level.player1.moves = 1
                if event.key == pygame.K_UP:
                    level.player2.moves = -1
                if event.key == pygame.K_DOWN:
                    level.player2.moves = 1

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    level.player1.moves = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    level.player2.moves = 0

        level.move_player(level.player1)
        level.move_player(level.player2)
        level.move_ball(2)

        render.draw()


if __name__ == "__main__":
    main()
