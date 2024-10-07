import sys
from settings import Settings
from ship import Ship
import game_functions
import pygame
def run_game():
    settings = Settings()
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ship = Ship(screen)

    pygame.display.set_caption("Alien Invasion")

    while True:
        game_functions.check_events(ship)
        ship.update()
        game_functions.update_screen(ship, screen, settings)


run_game()
