'''
	Игровой движок
'''
import controll as ctrl
import json
from pochito import Pochito

WIDTH = 900
HEIGHT = 500



def View(pygame, screen):
	'''
		Карта с играми
	'''
	FPS = 60
	clock = pygame.time.Clock()
	pochito = Pochito(screen, WIDTH // 2 - 150, HEIGHT // 2 + 50)

	game = True

	#	LOOP
	while game:
		clock.tick(FPS)

		ctrl.controll(pygame, screen, pochito)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				work = False
				pygame.quit()

		ctrl.updates(pygame, screen, pochito)
