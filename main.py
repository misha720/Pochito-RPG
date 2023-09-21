"""
	Pochito RPG
"""

# Import
import pygame
import layout__game as Game
import layout__menu as Menu

# Value
pygame.init()  # Инициализация

scene_menu = 0
scene_game = 2  # Установка сцены
activity = {
    'load': scene_menu,
    'name_level': ""
}

WIDTH = 700
HEIGHT = 500
FPS = 60


# Function
def engine():
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption('Pochito RPG')
    pygame.display.set_icon(pygame.image.load('pochito_ico.ico'))
    global activity  # В начале запустить

    while True:
        if activity['load'] == scene_menu:
        	activity['load'] = Menu.View(pygame, screen)

        # elif activity['load'] == scene_map:
        # 	activity = Map.View(pygame, screen)

        if activity['load'] == scene_game:
            # activity['load'] = Game.View(pygame, screen, str(activity['run_game']))
            activity['load'] = Game.View(pygame, screen)


# Run
if __name__ == '__main__':
    engine()
