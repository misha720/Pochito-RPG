"""
	Меню
"""

scene_menu = 0
scene_map = 1
scene_game = 2

def View(pygame, screen):
    FPS = 30
    clock = pygame.time.Clock()
    WIDTH = screen.get_rect().width
    HEIGHT = screen.get_rect().height

    background = pygame.transform.scale(pygame.image.load("src/menu/bg.png"), (WIDTH, HEIGHT))

    # pygame.mixer.init()
    # pygame.mixer.music.load('sound/menu.mp3')
    # pygame.mixer.music.set_volume(0.20)
    # pygame.mixer.music.play(-1)
    
    # BTN_ARCADE
    pygame.mouse.set_visible(False)
    cursor = pygame.transform.scale(pygame.image.load('src/cursor.png').convert_alpha(), 
            (50, 50))

    btn_arcade_w = WIDTH // 100 * 30
    btn_arcade_h = HEIGHT // 100 * 15

    btn_arcade = pygame.transform.scale(pygame.image.load('src/menu/item_arcade.png'), 
        (btn_arcade_w, btn_arcade_h))

    btn_arcade_posx = WIDTH - btn_arcade_w - 50
    btn_arcade_posy = HEIGHT - btn_arcade_h - 50

    #	LOOP
    menu = True
    while menu:
        clock.tick(FPS)
        screen.blit(background, (0,0))

        screen.blit(btn_arcade, (btn_arcade_posx, btn_arcade_posy))
        
        pos_curs = pygame.mouse.get_pos()
        x = pos_curs[0]
        y = pos_curs[1]
        screen.blit(cursor,(x,y-48))

        #	Обработчик событий
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    OnClick_mouse_pos = pygame.mouse.get_pos()
                    if OnClick_mouse_pos[0] >= btn_arcade_posx and OnClick_mouse_pos[0] <= btn_arcade_posx + btn_arcade_w:
                        if OnClick_mouse_pos[1] >= btn_arcade_posy and OnClick_mouse_pos[1] <= btn_arcade_posy + btn_arcade_h:
                            pygame.mixer.music.stop()
                            return scene_game


        keys = pygame.key.get_pressed()  # Получаем нажатые клавиши
        if keys[pygame.K_ESCAPE]:
            pygame.quit()

        pygame.display.flip()
