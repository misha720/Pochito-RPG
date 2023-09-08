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
	pygame.font.init()
	font_family = pygame.font.match_font("ubuntu")
	Font = pygame.font.Font(font_family, 100)

	pochito = Pochito(screen, WIDTH // 2 - 150, HEIGHT // 2 + 50)
	zombies = pygame.sprite.Group()

	ctrl.create_zombie(screen, zombies, 5)

	# pygame.mixer.music.load('sound/fight.mp3')
	# pygame.mixer.music.set_volume(1)
	# pygame.mixer.music.play(0)
	
	#	LOOP
	game = True
	while game:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				work = False
				pygame.quit()

		if pochito.health >= 1:

			ctrl.controll(pygame, screen, pochito, zombies)
			ctrl.updates(pygame, screen, pochito, zombies)
			zombies.update([pochito.x, pochito.y], pochito.check_attak)

		else:
			# Die
			print("You Count - " + str(pochito.kills_count))
			pygame.mixer.music.set_volume(0.2)
			screen.fill((0,0,0))
			text = Font.render("You Die...", 1, (255, 0, 0))
			screen.blit(text, (WIDTH // 2 - 300, HEIGHT // 2 - 100))
			pygame.display.flip()


		
