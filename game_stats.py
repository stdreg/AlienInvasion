class GameStats:
    # Track statistics for Alien Invastion

    def __init__(self,ai_game):       
        self.settings = ai_game.settings
        self.reset_status()
        self.game_active = True

    def reset_status(self):
        self.ships_left = self.settings.ship_limit

