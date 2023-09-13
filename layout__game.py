"""
	Игровой движок
"""
import controll as ctrl
from pochito import Pochito
from ui import UI

WIDTH = 900
HEIGHT = 500


def View(pygame, screen):
    """
		Карта с играми
	"""
    FPS = 60
    clock = pygame.time.Clock()

    pygame.font.init()
    font_family = pygame.font.match_font("ubuntu")

    ui_ctrl = UI(screen)
    pochito = Pochito(screen, WIDTH // 2 - 150, HEIGHT // 2 + 50)
    zombies = pygame.sprite.Group()

    ctrl.create_zombie(screen, zombies, 5)

    pygame.mixer.init()
    pygame.mixer.music.load('sound/fight.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(0)

    level_control = 0

    #	LOOP
    game = True
    while game:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

        if level_control == 0:  # OnGame
            if pochito.health >= 1:

                ctrl.controll(pygame, screen, pochito, zombies, ui_ctrl)
                ctrl.updates(pygame, screen, pochito, zombies, ui_ctrl)
                zombies.update([pochito.x, pochito.y], pochito.check_attak)
            else:
                level_control = 2

        elif level_control == 2:  # OnDie
            pygame.mixer.music.set_volume(0.2)
            screen.blit(pygame.image.load("src/bg.png"), (0, 0))  # Установка заднего фона

            Font = pygame.font.Font(font_family, 50)
            Font2 = pygame.font.Font(font_family, 40)
            text = Font.render("You Die", 1, (255, 0, 0))
            text_count = Font2.render("Count - " + str(pochito.kills_count), 1, (255, 0, 0))
            screen.blit(text, (WIDTH // 2 - text.get_width(), HEIGHT // 2 - text.get_height() - text_count.get_height() - 20))
            screen.blit(text_count, ( WIDTH // 2 - text_count.get_width(), HEIGHT // 2 - text_count.get_height()))

            pygame.display.flip()
