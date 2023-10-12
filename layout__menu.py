"""
	Меню
"""

def View(pygame, screen, config):
    clock = pygame.time.Clock()
    WIDTH = screen.get_rect().width
    HEIGHT = screen.get_rect().height

    background = pygame.transform.scale(pygame.image.load("src/menu/bg.png"), (WIDTH, HEIGHT))

    # Sound
    pygame.mixer.init()
    pygame.mixer.music.load('sound/menu.mp3')
    pygame.mixer.music.set_volume(config["settings"]["sound_volume"])
    pygame.mixer.music.play(-1)
    
    # Cursor
    pygame.mouse.set_visible(False)
    cursor = pygame.transform.scale(pygame.image.load('src/cursor.png').convert_alpha(), 
            (50, 50))

    # Button Arcade
    btn_arcade_size = [WIDTH // 100 * 30, HEIGHT // 100 * 15]
    btn_arcade = pygame.transform.scale(pygame.image.load('src/menu/item_arcade.png'), 
        (btn_arcade_size[0], btn_arcade_size[1]))
    btn_arcade_pos = [WIDTH - btn_arcade_size[0] - 50, HEIGHT - btn_arcade_size[1] - 50]

    #	LOOP
    menu = True
    while menu:
        clock.tick()

        # Draw Backgroud
        screen.blit(background, (0,0))
        # Draw Button Arcade
        screen.blit(btn_arcade, btn_arcade_pos)
        
        # Draw Cursor
        pos_curs = pygame.mouse.get_pos()
        screen.blit(cursor,(pos_curs[0],pos_curs[1]-48))

        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    OnClick_mouse_pos = pygame.mouse.get_pos()

                    # Button Arcade
                    if OnClick_mouse_pos[0] >= btn_arcade_pos[0] and OnClick_mouse_pos[0] <= btn_arcade_pos[0] + btn_arcade_size[0]:
                        if OnClick_mouse_pos[1] >= btn_arcade_pos[1] and OnClick_mouse_pos[1] <= btn_arcade_pos[1] + btn_arcade_size[1]:
                            
                            # Return to Game Arcade
                            pygame.mixer.music.stop()
                            config['work_scene'] = 'game'
                            return config

        # Exit
        keys = pygame.key.get_pressed()  # Получаем нажатые клавиши
        if keys[pygame.K_ESCAPE]:
            pygame.quit()

        # Update
        pygame.display.flip()
