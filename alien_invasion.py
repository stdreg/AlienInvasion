import sys
import pygame

class AlienInvasion:
    """Manage game assets and behavior"""
    def __init__(self):
        pygame.init()

        self.sceen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """main loop for the game"""
        while True:
            """keyboard and mouse events"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            """make most recent draw screen visible"""
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
