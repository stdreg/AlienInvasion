import pygame

class Ship:

    def __init__(self,ai_game):
        self.screen = ai_game.sceen
        self.screen_rect = ai_game.sceen.get_rect()

        # Load image
        self.image = pygame.image.loa("images/myship.myship.bmp")
        self.rect = self.image.get_rect()

        # Start earch new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image,self.rect)