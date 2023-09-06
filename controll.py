
from pochito import Pochito

def updates(pygame, screen, pochito):
	screen.blit( pygame.image.load("src/bg.png"), (0,0) ) # Установка заднего фона
	pochito.drawing()

	pygame.display.flip()

def pochito_check(pygame, screen, pochito):
	screen_rect = screen.get_rect() # Получаем границы экрана

def controll(pygame, screen, pochito):
	'''
		Контролер, действия после нажатия определённых клавиш
	'''
	keys = pygame.key.get_pressed() # Получаем нажатые клавиши

	if keys[pygame.K_a]: 
		# Left
		pochito.update([-1,0])
		updates(pygame, screen, pochito)

	if keys[pygame.K_w]: 
		# Top
		pochito.update([0,-1])
		updates(pygame, screen, pochito)

	if keys[pygame.K_d]: 
		# Right
		pochito.update([1,0])
		updates(pygame, screen, pochito)

	if keys[pygame.K_s]: 
		# Bottom
		pochito.update([0,1])
		updates(pygame, screen, pochito)
