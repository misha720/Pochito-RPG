
import random

from pochito import Pochito
from zombie import Zombie

def updates(pygame, screen, pochito, zombies):
	# UI
	screen.blit( pygame.image.load("src/bg.png"), (0,0) ) # Установка заднего фона

	pygame.font.init()
	font_family = pygame.font.match_font("ubuntu")
	Font = pygame.font.Font(font_family, 30)
	text = Font.render("Health - " + str(int(pochito.health)), 1, (0, 255, 0))
	text2 = Font.render("Kills - " + str(int(pochito.kills_count)), 1, (255, 0, 0))
	screen.blit(text, (10, 10))
	screen.blit(text2, (10, 40))

	# GAME
	pochito.drawing()

	# Check Health All Zombie
	for zombie in zombies.sprites():
		if zombie.health <= 0:
			if pochito.health <= 300: # Ограничение, что бы здоровья всегда было мало
				pochito.health += 50
			zombie.health = 100
			zombie.attak += 0.1
			print("Second Zombie Attak - " + str(zombie.attak))
			zombie.direction_slop = random.choice([-1,0,1])
			pochito.kills_count += 1

			random_pos_x = [random.randint(-200, -100), random.randint(900, 1000)]
			zombie.x = random_pos_x[random.randint(0, 1)]
			zombie.y = random.randint(200, 400)

		# Зомби атака в случае соприкосновения с игроком
		if pochito.rect.colliderect(zombie.rect):
			pochito.health -= zombie.attak
			
	zombies.draw(screen)

	pygame.display.flip()

def controll(pygame, screen, pochito, zombies):
	'''
		Контролер, действия после нажатия определённых клавиш
	'''
	keys = pygame.key.get_pressed() # Получаем нажатые клавиши

	# Move + Attak
	if keys[pygame.K_d] == True and keys[pygame.K_RIGHT] == True:
		# Move Right And Attak
		for zombie in zombies.sprites():
			if pochito.rect.colliderect(zombie.rect):
				zombie.health -= pochito.attak

		pochito.check_attak = True
		pochito.update([1,0], "right_attak")
		
		return

	elif keys[pygame.K_a] == True and keys[pygame.K_LEFT] == True:
		# Move Left And Attak
		for zombie in zombies.sprites():
			if pochito.rect.colliderect(zombie.rect):
				zombie.health -= pochito.attak

		pochito.check_attak = True
		pochito.update([-1,0], "left_attak")
		
		return

	# Move
	if keys[pygame.K_a] == True and keys[pygame.K_w] == True:
		# Left And Top
		pochito.check_attak = False
		pochito.update([-1,-1], "left")

		updates(pygame, screen, pochito, zombies)

	elif keys[pygame.K_w] == True and keys[pygame.K_d] == True:
		# Top And Right
		pochito.check_attak = False
		pochito.update([1,-1], "right")

		updates(pygame, screen, pochito, zombies)

	elif keys[pygame.K_d] == True and keys[pygame.K_s] == True:
		# Right And Bottom
		pochito.check_attak = False
		pochito.update([1,1], "right")

		updates(pygame, screen, pochito, zombies)

	elif keys[pygame.K_s] == True and keys[pygame.K_a] == True:
		# Bottom And Left
		pochito.check_attak = False
		pochito.update([-1,1], "left")

		updates(pygame, screen, pochito, zombies)

	if keys[pygame.K_a]: 
		# Left
		pochito.check_attak = False
		pochito.update([-1,0], "left")

		updates(pygame, screen, pochito, zombies)

	elif keys[pygame.K_w]: 
		# Top
		pochito.check_attak = False
		pochito.update([0,-1], pochito.direction)

		updates(pygame, screen, pochito, zombies)

	elif keys[pygame.K_d]: 
		# Right
		pochito.check_attak = False
		pochito.update([1,0], "right")

		updates(pygame, screen, pochito, zombies)

	elif keys[pygame.K_s]: 
		# Bottom
		pochito.check_attak = False
		pochito.update([0,1], pochito.direction)

		updates(pygame, screen, pochito, zombies)

	else:
		pochito.check_attak = False
		pochito.image_anim_count = 0

		updates(pygame, screen, pochito, zombies)

def create_zombie(screen, zombies, count_zombie: int):

	for item in range(count_zombie):
		random_pos_x = [random.randint(-200, -100), random.randint(900, 1000)]

		pos_x = random_pos_x[random.randint(0, 1)]
		pos_y = random.randint(200, 400)

		# Create object Zombie
		zombie = Zombie(screen, pos_x, pos_y)
		zombies.add(zombie)
