import json

def View(pygame, screen, config):
    # Settings
    clock = pygame.time.Clock()
    WIDTH = screen.get_rect().width
    HEIGHT = screen.get_rect().height
    
    # Config
    with open('config.json', 'r') as fconfig:
        config = json.load(fconfig)

    # Font 
    pygame.font.init()
    font_family = pygame.font.match_font("ubuntu")

    # Background
    bg_history = pygame.transform.scale(pygame.image.load("src/menu/bg_history.png"), (WIDTH, HEIGHT))
    bg_arcade = pygame.transform.scale(pygame.image.load("src/menu/bg_arcade.png"), (WIDTH, HEIGHT))

    # Sound
    pygame.mixer.init()
    pygame.mixer.music.load('sound/menu.mp3')
    pygame.mixer.music.set_volume(config["settings"]["sound_volume"])
    pygame.mixer.music.play(-1)
    
    # Cursor
    pygame.mouse.set_visible(False)
    cursor = pygame.transform.scale(pygame.image.load('src/cursor.png').convert_alpha(), 
            (50, 50))

    # Button Image
    btn_item_size = [WIDTH // 100 * 20, HEIGHT // 100 * 10]
    btn_item = pygame.transform.scale(pygame.image.load('src/menu/item.png').convert_alpha(), 
        (btn_item_size[0], btn_item_size[1]))
    btn_item_pos = [0,0]

    # Grid Buttons
    grid_buttons = [
        [0, HEIGHT // 2 - btn_item_size[1] * 2],
        [0, HEIGHT // 2 - btn_item_size[1]],
        [0, HEIGHT // 2],
        [0, HEIGHT // 2 + btn_item_size[1]]
    ]

    # Items

    # History
    Font = pygame.font.Font(font_family, 40)
    item_history = Font.render("History", 1, (255, 255, 255))
    item_history_pos = [
        btn_item.get_rect().centerx - item_history.get_rect().width // 2,
        grid_buttons[0][1] + btn_item.get_rect().centery - item_history.get_rect().height // 2]
    item_history_active = True

    # Arcade
    Font = pygame.font.Font(font_family, 40)
    item_arcade = Font.render("Arcade", 1, (255, 255, 255))
    item_arcade_pos = [
        btn_item.get_rect().centerx - item_arcade.get_rect().width // 2,
        grid_buttons[1][1] + btn_item.get_rect().centery - item_arcade.get_rect().height // 2]
    item_arcade_active = False
    
    # Tuning
    Font = pygame.font.Font(font_family, 40)
    item_tuning = Font.render("Tuning", 1, (255, 255, 255))
    item_tuning_pos = [
        btn_item.get_rect().centerx - item_arcade.get_rect().width // 2,
        grid_buttons[2][1] + btn_item.get_rect().centery - item_arcade.get_rect().height // 2]
    item_tuning_active = False
    
    # Settings
    Font = pygame.font.Font(font_family, 40)
    item_settings = Font.render("Settings", 1, (255, 255, 255))
    item_settings_pos = [
        btn_item.get_rect().centerx - item_arcade.get_rect().width // 2,
        grid_buttons[3][1] + btn_item.get_rect().centery - item_arcade.get_rect().height // 2]
    item_settings_active = False

    # Button Arcade Start
    Font = pygame.font.Font(font_family, 30)
    item_arcade_start = Font.render("Go!", 1, (255, 255, 255))
    btn_arcade_start = pygame.transform.rotate(btn_item, 180)
    btn_arcade_start_pos = [
        WIDTH - btn_arcade_start.get_rect().width,
        HEIGHT - btn_arcade_start.get_rect().height * 2
    ]

    # Text for Arcade
    text_arcade = "Любите ли Вы, причинять боль другим? Да? Тогда режим 'Аркада' именно для тебя!"
    text_arcade2 = "Вся хронология с теми же самыми боссами и врагами под классный саундтрек. Вперёд!"
    Font = pygame.font.Font(font_family, 20)
    item_text_arcade = Font.render(text_arcade, 1, (255, 255, 255))
    item_text_arcade2 = Font.render(text_arcade2, 1, (255, 255, 255))
    item_text_arcade_pos = [
        WIDTH // 100 * 30,
        HEIGHT // 100 * 20]

    #	LOOP
    menu = True
    while menu:
        clock.tick()

        # Draw Backgroud
        if item_history_active:
            screen.blit(bg_history, (0,0))
        if item_arcade_active:
            screen.blit(bg_arcade, (0,0))
        if item_tuning_active:
            screen.blit(bg_history, (0,0))
        if item_settings_active:
            screen.blit(bg_history, (0,0))


        # Draw Button Image
        if item_history_active:
            screen.blit(btn_item, grid_buttons[0])
        # Draw Button Image
        if item_arcade_active:
            screen.blit(btn_item, grid_buttons[1])
        # Draw Button Image
        if item_tuning_active:
            screen.blit(btn_item, grid_buttons[2])
        # Draw Button Image
        if item_settings_active:
            screen.blit(btn_item, grid_buttons[3])


        # Draw Item History
        screen.blit(item_history, item_history_pos)
        # Draw Item Arcade
        screen.blit(item_arcade, item_arcade_pos)
        # Draw Item Tuning
        screen.blit(item_tuning, item_tuning_pos)
        # Draw Item Settings
        screen.blit(item_settings, item_settings_pos)

        # Draw Button Arcade Start
        if item_arcade_active:
            
            # Draw Button
            screen.blit(btn_arcade_start, btn_arcade_start_pos)
            
            # Draw Text
            screen.blit( item_arcade_start, (
                btn_arcade_start_pos[0] + btn_arcade_start.get_rect().centerx - item_arcade_start.get_rect().width // 2,
                btn_arcade_start_pos[1] + btn_arcade_start.get_rect().centery - item_arcade_start.get_rect().height // 2) )

            screen.blit(item_text_arcade, item_text_arcade_pos)
            screen.blit(item_text_arcade2, (
                item_text_arcade_pos[0],
                item_text_arcade_pos[1] + item_text_arcade.get_rect().height + 10 ))

        # Draw Cursor
        pos_curs = pygame.mouse.get_pos()
        screen.blit(cursor,(pos_curs[0],pos_curs[1]-48))

        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    OnClick_mouse_pos = pygame.mouse.get_pos()

                    # Button History
                    if OnClick_mouse_pos[0] >= grid_buttons[0][0] and OnClick_mouse_pos[0] <= grid_buttons[0][0] + btn_item_size[0]:
                        if OnClick_mouse_pos[1] >= grid_buttons[0][1] and OnClick_mouse_pos[1] <= grid_buttons[0][1] + btn_item_size[1]:
                            item_history_active = True
                            item_arcade_active = False
                            item_tuning_active = False
                            item_settings_active = False

                    # Button Arcade
                    if OnClick_mouse_pos[0] >= grid_buttons[1][0] and OnClick_mouse_pos[0] <= grid_buttons[1][0] + btn_item_size[0]:
                        if OnClick_mouse_pos[1] >= grid_buttons[1][1] and OnClick_mouse_pos[1] <= grid_buttons[1][1] + btn_item_size[1]:
                            item_history_active = False
                            item_arcade_active = True
                            item_tuning_active = False
                            item_settings_active = False

                    # Button Tuning
                    if OnClick_mouse_pos[0] >= grid_buttons[2][0] and OnClick_mouse_pos[0] <= grid_buttons[2][0] + btn_item_size[0]:
                        if OnClick_mouse_pos[1] >= grid_buttons[2][1] and OnClick_mouse_pos[1] <= grid_buttons[2][1] + btn_item_size[1]:
                            item_history_active = False
                            item_arcade_active = False
                            item_tuning_active = True
                            item_settings_active = False

                    # Button Cursor
                    if OnClick_mouse_pos[0] >= grid_buttons[3][0] and OnClick_mouse_pos[0] <= grid_buttons[3][0] + btn_item_size[0]:
                        if OnClick_mouse_pos[1] >= grid_buttons[3][1] and OnClick_mouse_pos[1] <= grid_buttons[3][1] + btn_item_size[1]:
                            item_history_active = False
                            item_arcade_active = False
                            item_tuning_active = False
                            item_settings_active = True

                    if item_arcade_active:
                        if OnClick_mouse_pos[0] >= btn_arcade_start_pos[0] and OnClick_mouse_pos[0] <= btn_arcade_start_pos[0] + btn_item_size[0]:
                            if OnClick_mouse_pos[1] >= btn_arcade_start_pos[1] and OnClick_mouse_pos[1] <= btn_arcade_start_pos[1] + btn_item_size[1]:
                                # Return to Game Arcade
                                pygame.mixer.music.stop()
                                config["work_scene"] = "arcade"
                                return config
        # Exit
        keys = pygame.key.get_pressed()  # Получаем нажатые клавиши
        if keys[pygame.K_ESCAPE]:
            pygame.quit()

        # Update
        pygame.display.flip()
