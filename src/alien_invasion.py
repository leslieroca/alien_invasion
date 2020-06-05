import pygame
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
    ship = Ship(screen)
    

    # Start the main loop for the game.
    while True:
        # Sets redraw at 60 FPS
        clock.tick(60)
        
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)

        
run_game()