import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functios as gf



def run_game():

    # Initialize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.screen_mode)
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()
    

    # Start the main loop for the game.
    while True:
        # Sets redraw at 60 FPS
        clock.tick(60)
        
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

        
run_game()