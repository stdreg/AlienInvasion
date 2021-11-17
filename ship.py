import pygame

class Ship:

    def __init__(self,ai_game):
        self.screen = ai_game.sceen
        self.screen_rect = ai_game.sceen.get_rect()

        # Load image
        self.image = pygame.image.load("images/myship.bmp")
        self.rect = self.image.get_rect()

        # Start earch new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Movement-Flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and (self.rect.x + self.rect.width) < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.x > self.screen_rect.left:
            self.rect.x -= 1            

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image,self.rect)