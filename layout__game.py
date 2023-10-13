"""
	Игровой движок
"""
import time

import controll as ctrl
from pochito import Pochito
from demon_zombie import ZombieDemon
from ui import UI
from ZombieDemonWeapon import ZombieDemonWeapon

def View(pygame, screen, config):
    """
		Карта с играми
	"""
    clock = pygame.time.Clock()
    FPS = 0
    WIDTH = screen.get_rect().width
    HEIGHT = screen.get_rect().height
    
    pochito = Pochito(screen, [WIDTH // 2, HEIGHT // 2])
    zombies = pygame.sprite.Group()
    zombie_demon = ZombieDemon(screen, WIDTH, HEIGHT // 100 * 20)
    zombie_demon_weapon = ZombieDemonWeapon(screen)
    ui_ctrl = UI(screen, time.time(), pochito)

    ctrl.create_zombie(screen, zombies, 5)

    # Sound
    pygame.mixer.init()
    pygame.mixer.music.load('sound/fight.mp3')
    pygame.mixer.music.set_volume(config["settings"]["sound_volume"])
    pygame.mixer.music.play(-1)

    round_timer = time.time()
    round_game = 0 # Какой раунд сейчас в игре

    #	LOOP
    game = True
    while game:
        clock.tick()
        FPS = clock.get_fps()
        #print(FPS)

        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

        ctrl.controll(pygame, screen, pochito)
        ctrl.updates(pygame, screen, config, FPS, pochito, zombies, ui_ctrl, zombie_demon, zombie_demon_weapon)
        zombies.update(FPS, [pochito.x, pochito.y], pochito.check_attak, [pochito.rect.width,pochito.rect.height])

            
