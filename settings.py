class Settings:
    
    def __init__(self):
        # Screen Settings
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (230,230,230)
        
        # Ship Settings        
        self.ship_limit = 3

        # Bullet Settings        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        # Alien settings        
        self.alien_drop_speed = 10        

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.bullet_speed = 1.5
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        # direction 1 = right, -1 = left
        self.fleet_direction = 1
        self.alien_points = 50
    
    def increase_speed(self):
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
        # direction 1 = right, -1 = left
        self.fleet_direction = 1
