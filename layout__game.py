"""
	Игровой движок
"""
import time

import controll as ctrl
from pochito import Pochito
from ui import UI

def View(pygame, screen):
    """
		Карта с играми
	"""
    FPS = 30
    clock = pygame.time.Clock()
    WIDTH = screen.get_rect().width
    HEIGHT = screen.get_rect().height

    pygame.font.init()

    ui_ctrl = UI(screen)
    pochito = Pochito(screen, WIDTH // 2, HEIGHT // 2)
    zombies = pygame.sprite.Group()

    ctrl.create_zombie(screen, zombies, 5)

    # pygame.mixer.init()
    # pygame.mixer.music.load('sound/fight.mp3')
    # pygame.mixer.music.set_volume(1)
    # pygame.mixer.music.play(-1)

    round_timer = time.time()
    round_game = 0 # Какой раунд сейчас в игре

    #	LOOP
    game = True
    while game:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

        second_round = time.time() - round_timer # Секунд прошло с начала игры

        if second_round >= 60:
            ctrl.create_zombie(screen, zombies, 5)
            round_timer = time.time()
            round_game += 1

        ctrl.controll(pygame, screen, pochito, zombies, ui_ctrl)
        ctrl.updates(pygame, screen, pochito, zombies, ui_ctrl)
        zombies.update([pochito.x, pochito.y], pochito.check_attak, [pochito.rect.width,pochito.rect.height])

            
