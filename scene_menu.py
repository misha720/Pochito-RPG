
def SceneMenu(pygame, screen, config):
	FPS = 60
	clock = pygame.time.Clock()
	width = screen.get_rect().width
	height = screen.get_rect().height

	# Background
	background = pygame.transform.scale(pygame.image.load("src/menu/bg.png"),
			(width, height))

	# Sound
	pygame.mixer.init()
	pygame.mixer.music.load('sound/menu.mp3')
	pygame.mixer.music.set_volume(config['sound_volme'])
	pygame.mixer.music.play(-1)

	# Mouse
	pygame.mouse.set_visible(False)
	cursor = pygame.transform.scale(pygame.image.load('src/cursor.png').convert_alpha(), 
			(50, 50))

	# Button "Arcade"
	btn_arcade_size = [width // 100 * 30, height // 100 * 15] # Size
	btn_arcade_pos = [width - btn_arcade_size[0] - 50, height - btn_arcade_size[1] - 50] # Position
	btn_arcade = pygame.transform.scale(pygame.image.load('src/menu/item_arcade.png'), 
			btn_arcade_size) # Image

	work = True
	while work:
		clock.tick(FPS)

		screen.blit(background, (0,0)) # Background
		screen.blit(btn_arcade, btn_arcade_pos) # Button "Arcade"
			
		second_position_cursor = pygame.mouse.get_pos() # Get Position Cursor
		screen.blit(cursor,
				(second_position_cursor[0], second_position_cursor[1] - 48)) # Cursor

		# Event Handler
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN: # OnClickMouse
				if event.button == 1:
					if second_position_cursor[0] >= btn_arcade_pos[0] and second_position_cursor[0] <= btn_arcade_pos[0] + btn_arcade_w:
						if second_position_cursor[1] >= btn_arcade_pos[1] and second_position_cursor[1] <= btn_arcade_pos[1] + btn_arcade_h:
							pygame.mixer.music.stop()
							config['view'] == "game"
							config['level'] == "arcade"
							return config

		keys = pygame.key.get_pressed()  # Получаем нажатые клавиши
		if keys[pygame.K_ESCAPE]:
			pygame.quit()

		pygame.display.flip()



