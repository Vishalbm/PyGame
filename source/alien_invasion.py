import sys

import pygame
def run_game():
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    screen.fill((230, 230, 230))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit("Exiting Game!")

        pygame.display.flip()


run_game()