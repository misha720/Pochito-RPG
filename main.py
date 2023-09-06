'''
	Pochito RPG
'''

#	Import
import pygame
import layout__game as Game

#	Value
pygame.init() # Инициализация
scene_game = 0 # Установка сцены 
activity = {
	'load':scene_game,
	'name_level':""
}

WIDTH = 700
HEIGHT = 500
FPS = 60

#	Function
def engine():
	screen = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption('Pochito RPG')
	global activity # В начале запустить

	while True:
		# if activity['load'] == scene_menu:
		# 	activity['load'] = Menu.View(pygame, screen)

		# elif activity['load'] == scene_map:
		# 	activity = Map.View(pygame, screen)

		if activity['load'] == scene_game:
			#print("Running - " + activity['run_game'])
			#activity['load'] = Game.View(pygame, screen, str(activity['run_game']))
			activity['load'] = Game.View(pygame, screen)

#	Run
if __name__ == '__main__':
	engine()