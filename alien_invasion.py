import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Manage game assets and behavior"""
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.sceen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_heigth))
        #set the caption        
        pygame.display.set_caption("Alien Invasion")
        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """main loop for the game"""
        while True:
            """keyboard and mouse events"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.sceen.fill(self.settings.bg_color)
            #make most recent draw screen visible
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
