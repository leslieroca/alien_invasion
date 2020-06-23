class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.screen_mode = (self.screen_width, self.screen_height)
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 3.5

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = (139, 69, 13)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1