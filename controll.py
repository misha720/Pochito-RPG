import random
import time

from zombie import Zombie


def updates(pygame, screen, config, FPS, pochito, zombies, ui, zombie_demon, zombie_demon_weapon):
    WIDTH = screen.get_rect().width
    HEIGHT = screen.get_rect().height
    
    if pochito.is_alive():
        # Alive         

        ui.drawing()
        
        # Round Update
        if ui.round_game != ui.minute_since_past_round:
            ui.round_game += 1
            create_zombie(screen, zombies, 5)

        # Called Boss
        if ui.round_game == 3 and zombie_demon.called == False:
            # Даём сигнал
            signal_to_boss = pygame.mixer.Sound("sound/signal_boss.wav")
            signal_to_boss.set_volume(config["settings"]["sound_volume"])
            signal_to_boss.play(0)
            ui.is_signed_worked = True
            
            # Призываем боса
            zombie_demon.called = True
            zombie_demon.time_called = time.time()



        # Boss
        if zombie_demon.called:
            recharge_boss_shot = time.time() - zombie_demon.time_called # Замеряется время с последнего выстрела
            if recharge_boss_shot >= 10: # Перезарядка 20 сек 
                zombie_demon.status = "attak"
                zombie_demon.time_called = time.time()

            #Boss Attak
            if pochito.rect.colliderect(zombie_demon.rect):
                if zombie_demon.is_used_weapon == False:
                    if pochito.status['hit']:
                        zombie_demon.health -= pochito.attak_hit
                            
                    if pochito.status['super']:
                        zombie_demon.health -= pochito.attak_super_hit

            if pochito.rect.colliderect(zombie_demon_weapon.weapon_rect):
                if zombie_demon.is_used_weapon == True:
                    pochito.health -= zombie_demon.attak
                    ui.shake_screen()


        pochito.update(FPS)
        zombie_demon.update(FPS, [pochito.x + pochito.rect.width // 2, pochito.y + pochito.rect.height // 2])
        zombie_demon_weapon.update(zombie_demon)

        # GAME

        # Проверка жизней каждого Зомби
        for zombie in zombies.sprites():
            if zombie.health <= 0:
                # Зомби умирает
                zombie.status = "die"
                if zombie.count_frame_die == len(zombie.die_frames)-1:

                    if pochito.health <= 100:  # Ограничение, что бы здоровья всегда было мало
                        pochito.health += 10

                    # Восстанавливаем зомби
                    zombie.health = 100
                    zombie.direction_slop = random.choice([-1, 0, 1])
                    zombie.status = "move"
                    zombie.count_frame_move = 0
                    zombie.count_frame_attak = 0
                    zombie.count_frame_die = 0
                    zombie.delay_move = 0
                    zombie.delay_attak = 0
                    zombie.delay_die = 0
                    pochito.kills_count += 1

                    random_pos_x = [random.randint(-screen.get_rect().width // 100 * 10, 0), 
                        random.randint(screen.get_rect().width, screen.get_rect().width + screen.get_rect().width // 100 * 10)]
                    zombie.x = random_pos_x[random.randint(0, 1)]
                    zombie.y = random.randint((screen.get_rect().height // 100 * 50) + (screen.get_rect().width // 100 * 10), 
                        screen.get_rect().height - (screen.get_rect().width // 100 * 10))

            # Атака зомби в случае соприкосновения с игроком
            elif pochito.rect.colliderect(zombie.rect):
                if zombie.rect.bottom in range( pochito.rect.bottom -50, pochito.rect.bottom + 50):
                    if pochito.status['hit']:
                        zombie.health -= pochito.attak_hit
                    
                    if pochito.status['super']:
                        zombie.health -= pochito.attak_super_hit

                    if zombie.first_contact == 0:
                        zombie.first_contact = time.time()
                        zombie.status = "attak"
                    
                    else:
                        resume = time.time() - zombie.first_contact 
                        if resume >= 1:
                            zombie.first_contact = 0
                            pochito.health -= zombie.attak
                            ui.shake_screen()
            else:
                zombie.status = "move"

        zombies.draw(screen)
        pochito.drawing()
        zombie_demon.drawing()
        zombie_demon_weapon.drawing()

    else:
        # No Alive
        ui.drawing()

        if pochito.is_alive():
            pochito.kill()

        # Sound
        if config['settings']['sound_volume'] >= 0.2:
            pygame.mixer.music.set_volume(config['settings']['sound_volume'] - 0.2)
        else:
            pygame.mixer.music.set_volume(config['settings']['sound_volume'])
        
    
    # Update Screen
    pygame.display.flip()
	
def controll(pygame, screen, config, pochito):
    """
        Контролер, действия после нажатия определённых клавиш
    """
    keys = pygame.key.get_pressed()  # Получаем нажатые клавиши

    if keys[pygame.K_ESCAPE]:
        config["work_scene"] = "menu"
        return

    if keys[pygame.K_UP] == False:
        if pochito.energy < 100:
            pochito.energy += 0.1
        pochito.status['super'] = False

    # Simple Hit + Move Left
    if keys[pygame.K_LEFT] == True and keys[pygame.K_a] == True:
        pochito.status['hit'] = True
        pochito.status['super'] = False
        pochito.check_attak = True
        pochito.status['move_x'] = -1
        pochito.direction = "left"
        return

    # Simple Hit + Move Right
    elif keys[pygame.K_LEFT] == True and keys[pygame.K_d] == True:
        pochito.status['hit'] = True
        pochito.status['super'] = False
        pochito.check_attak = True
        pochito.status['move_x'] = 1
        pochito.direction = "right"
        return

    # Simple Hit (Простой удар)
    elif keys[pygame.K_LEFT]:
        pochito.status['hit'] = True
        pochito.status['super'] = False
        pochito.check_attak = True
        pochito.status['move_x'] = 0
        pochito.status['move_y'] = 0

        return

    else:
        pochito.status['hit'] = False
        pochito.check_attak = False

    # Super Hit
    if keys[pygame.K_UP]:
        if not keys[pygame.K_LEFT]:
            if int(pochito.energy) > 0:
                pochito.status['super'] = True
                pochito.status['hit'] = False
                pochito.check_attak = True
                pochito.energy -= 0.2

                if pochito.direction == "right":
                    pochito.status['move_x'] = 5
                else:
                    pochito.status['move_x'] = -5

                pochito.status['move_y'] = 0

            else:
                pochito.status['super'] = False
                pochito.check_attak = False
                pochito.status['move_x'] = 0
                pochito.status['move_y'] = 0

        return

    # Move Top + Move Right
    if keys[pygame.K_w] == True and keys[pygame.K_d]:
        pochito.status['move_x'] = 1
        pochito.status['move_y'] = -1
        pochito.direction = "right"
        return

    # Move Right + Move Bottom
    elif keys[pygame.K_d] == True and keys[pygame.K_s]:
        pochito.status['move_x'] = 1
        pochito.status['move_y'] = 1
        pochito.direction = "right"
        return

    # Move Bottom + Move Left
    elif keys[pygame.K_s] == True and keys[pygame.K_a]:
        pochito.status['move_x'] = -1
        pochito.status['move_y'] = 1
        pochito.direction = "left"
        return

    # Move Left + Move Top
    elif keys[pygame.K_a] == True and keys[pygame.K_w]:
        pochito.status['move_x'] = -1
        pochito.status['move_y'] = -1
        pochito.direction = "left"
        return

    # Top
    elif keys[pygame.K_w]:
        pochito.status['move_x'] = 0
        pochito.status['move_y'] = -1
        return

    # Right
    elif keys[pygame.K_d]:
        pochito.status['move_x'] = 1
        pochito.status['move_y'] = 0
        pochito.direction = "right"
        return

    # Bottom
    elif keys[pygame.K_s]:
        pochito.status['move_x'] = 0
        pochito.status['move_y'] = 1
        return

    # Left
    elif keys[pygame.K_a]:
        pochito.status['move_x'] = -1
        pochito.status['move_y'] = 0
        pochito.direction = "left"
        return

    else:  
        pochito.status['move_x'] = 0
        pochito.status['move_y'] = 0
        pochito.status['hit'] = False
        pochito.check_attak = False
        return


def create_zombie(screen, zombies, count_zombie: int):
    """
        Функция генерирует зомби в заданном колличестве `count_zombie`
    """

    for item in range(count_zombie):
        random_pos_x = [random.randint(-screen.get_rect().width // 100 * 10, 0), 
            random.randint(screen.get_rect().width, screen.get_rect().width + screen.get_rect().width // 100 * 10)]

        pos_x = random_pos_x[random.randint(0, 1)]
        pos_y = random.randint((screen.get_rect().height // 100 * 50) + (screen.get_rect().width // 100 * 10), 
            screen.get_rect().height - (screen.get_rect().width // 100 * 10))

        # Создание и добавление зомби
        zombie = Zombie(screen, pos_x, pos_y)
        zombies.add(zombie)
