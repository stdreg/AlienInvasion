class Settings:
    
    def __init__(self):
        # Screen Settings
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (230,230,230)
        
        # Ship Settings
        self.ship_speed = 2.0
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.alien_drop_speed = 50
        # direction 1 = right, -1 = left
        self.fleet_direction = 1