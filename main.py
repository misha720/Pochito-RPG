"""
	Pochito RPG
"""

# Import
import pygame
import json

# Connect
import layout__game as Game
import layout__menu as Menu
        
# PyGame   
pygame.init()  # Инициализация


# Main
def main():
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption('Pochito RPG')
    pygame.display.set_icon(pygame.image.load('pochito_ico.ico'))
    
    with open('config.json', 'r') as fconfig:
        config = json.load(fconfig)

    while True:
        if config['work_scene'] == "menu":
        	config = Menu.View(pygame, screen, config)

        if config['work_scene'] == "game":
            config = Game.View(pygame, screen, config)


# Run
if __name__ == '__main__':
    main()
