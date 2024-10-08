import pygame
class Ship():
    def __init__(self, screen):
        self.screen = screen
        # Load the ship image and get its rect.
        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.ship_speed_factor = 1.5

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1 * self.ship_speed_factor
        if self.moving_left:
            self.rect.centerx -= 1 * self.ship_speed_factor
