import pygame


def handle_input(key):
    if key == pygame.K_w:
        pass


class Events:
    def __init__(self):
        pass

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                pass
