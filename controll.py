
import random

from pochito import Pochito
from zombie import Zombie

def updates(pygame, screen, pochito, zombies):
	screen.blit( pygame.image.load("src/bg.png"), (0,0) ) # Установка заднего фона
	pochito.drawing()
	zombies.draw(screen)

	pygame.display.flip()

def pochito_check(pygame, screen, pochito):
	screen_rect = screen.get_rect() # Получаем границы экрана

def controll(pygame, screen, pochito, zombies):
	'''
		Контролер, действия после нажатия определённых клавиш
	'''
	keys = pygame.key.get_pressed() # Получаем нажатые клавиши

	if keys[pygame.K_a]: 
		# Left
		pochito.update([-1,0], "left")
		updates(pygame, screen, pochito, zombies)

	elif keys[pygame.K_w]: 
		# Top
		pochito.update([0,-1], "top")
		updates(pygame, screen, pochito, zombies)

	elif keys[pygame.K_d]: 
		# Right
		pochito.update([1,0], "right")
		updates(pygame, screen, pochito, zombies)

	elif keys[pygame.K_s]: 
		# Bottom
		pochito.update([0,1], "bottom")
		updates(pygame, screen, pochito, zombies)

	else:
		pochito.image_anim_count = 0
		updates(pygame, screen, pochito, zombies)

def create_zombie(screen, zombies):

	for item in range(4):
		pos_x = random.randint(900, 1000)
		pos_y = random.randint(200, 400)

		# Create object Zombie
		zombie = Zombie(screen, pos_x, pos_y)
		zombies.add(zombie)
