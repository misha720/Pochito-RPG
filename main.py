"""
	Pochito RPG v1
	Powered by Zero, SCH
"""

# Import
import pygame
import json

import scene_menu as SceneMenu
#from scene_level import SceneLevel

class Main():
	def __init__(self):
		pygame.init()

		# Load config file
		with open('config.json', 'r') as fconfig:
			config = json.load(fconfig)

		# Screen
		screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		pygame.display.set_caption('Pochito RPG')
		pygame.display.set_icon(pygame.image.load('pochito_ico.ico'))

		while True:
			if config['view'] == "menu":
				config = SceneMenu.SceneMenu(pygame, screen, config)
			elif config['view'] == "level":
				config = SceneLevel(pygame, screen, config, config['level'])

# Run
if __name__ == '__main__':
    Main()
		
