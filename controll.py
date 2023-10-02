import random
import time

from zombie import Zombie


def updates(pygame, screen, pochito, zombies, ui):
    font_family = pygame.font.match_font("ubuntu")
    WIDTH = screen.get_rect().width
    HEIGHT = screen.get_rect().height
    
    if pochito.health >= 1:
        # On Live
        
        # UI
        ui.drawing(pochito.health)
        pochito.update()

        # GAME

        # Проверка жизней каждого Зомби
        for zombie in zombies.sprites():
            if zombie.health <= 0:
                # Зомби умирает
                zombie.status = "die"
                if zombie.image_anim_count == len(zombie.die_images)-1:

                    if pochito.health <= 100:  # Ограничение, что бы здоровья всегда было мало
                        pochito.health += 10

                    # Восстанавливаем зомби
                    zombie.health = 100
                    zombie.direction_slop = random.choice([-1, 0, 1])
                    zombie.status = "move"
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

        pygame.display.flip()

    else:
        # On Die
        pygame.mixer.music.set_volume(0.2)
        screen.blit(pygame.transform.scale(pygame.image.load("src/bg.png").convert_alpha(), (screen.get_rect().width, screen.get_rect().height)), (0, 0))  # Установка заднего фона

        Font = pygame.font.Font(font_family, 50)
        Font2 = pygame.font.Font(font_family, 40)
        text = Font.render("You Die", 1, (255, 0, 0))
        text_count = Font2.render("Count - " + str(pochito.kills_count), 1, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width(), HEIGHT // 2 - text.get_height() - text_count.get_height() - 20))
        screen.blit(text_count, ( WIDTH // 2 - text_count.get_width(), HEIGHT // 2 - text_count.get_height()))

        pygame.display.flip()
	
def controll(pygame, screen, pochito, zombies, ui):
    """
        Контролер, действия после нажатия определённых клавиш
    """
    keys = pygame.key.get_pressed()  # Получаем нажатые клавиши

    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    # Simple Hit + Move Left
    if keys[pygame.K_LEFT] == True and keys[pygame.K_a] == True:
        pochito.status['hit'] = True
        pochito.check_attak = True
        pochito.status['move_x'] = -1
        pochito.direction = "left"
        return

    # Simple Hit + Move Right
    elif keys[pygame.K_LEFT] == True and keys[pygame.K_d] == True:
        pochito.status['hit'] = True
        pochito.check_attak = True
        pochito.status['move_x'] = 1
        pochito.direction = "right"
        return

    # Simple Hit (Простой удар)
    elif keys[pygame.K_LEFT]:
        pochito.status['hit'] = True
        pochito.check_attak = True
        pochito.status['move_x'] = 0
        pochito.status['move_y'] = 0

        return

    else:
        pochito.status['hit'] = False
        pochito.check_attak = False

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

    # if keys[pygame.K_RIGHT] == True and keys[pygame.K_d] == True:
    #     # Движение вправо и атака
    #     for zombie in zombies.sprites():
    #         if pochito.rect.colliderect(zombie.rect):
    #             if zombie.rect.bottom in range( pochito.rect.bottom -50, pochito.rect.bottom + 50):
    #                 zombie.health -= pochito.attak

    #     pochito.check_attak = True
    #     pochito.update([1, 0], "right_attak")

    #     return

    # elif keys[pygame.K_LEFT] == True and keys[pygame.K_a] == True:
    #     # Движение влево и атака
    #     for zombie in zombies.sprites():
    #         if pochito.rect.colliderect(zombie.rect):
    #             if zombie.rect.bottom in range( pochito.rect.bottom -50, pochito.rect.bottom + 50):
    #                 zombie.health -= pochito.attak

    #     pochito.check_attak = True
    #     pochito.update([-1, 0], "left_attak")

    #     return

    # # Attak
    # elif keys[pygame.K_RIGHT] == True:
    #     # Движение вправо и атака
    #     for zombie in zombies.sprites():
    #         if pochito.rect.colliderect(zombie.rect):
    #             if zombie.rect.bottom in range( pochito.rect.bottom -50, pochito.rect.bottom + 50):
    #                 zombie.health -= pochito.attak

    #     pochito.check_attak = True
    #     pochito.update([0, 0], "right_attak")

    #     return

    # elif keys[pygame.K_LEFT] == True:
    #     # Движение влево и атака
    #     for zombie in zombies.sprites():
    #         if pochito.rect.colliderect(zombie.rect):
    #             if zombie.rect.bottom in range( pochito.rect.bottom -50, pochito.rect.bottom + 50):
    #                 zombie.health -= pochito.attak

    #     pochito.check_attak = True
    #     pochito.update([0, 0], "left_attak")

    #     return

    # # Move
    # elif keys[pygame.K_a] == True and keys[pygame.K_w] == True:
    #     # Движение в лево-вверх
    #     pochito.check_attak = False
    #     pochito.update([-1, -1], "left")

    #     updates(pygame, screen, pochito, zombies, ui, bloods)

    # elif keys[pygame.K_w] == True and keys[pygame.K_d] == True:
    #     # Движение вверх-право
    #     pochito.check_attak = False
    #     pochito.update([1, -1], "right")

    #     updates(pygame, screen, pochito, zombies, ui, bloods)

    # elif keys[pygame.K_d] == True and keys[pygame.K_s] == True:
    #     # Движение в право-вниз
    #     pochito.check_attak = False
    #     pochito.update([1, 1], "right")

    #     updates(pygame, screen, pochito, zombies, ui, bloods)

    # elif keys[pygame.K_s] == True and keys[pygame.K_a] == True:
    #     # Движение в лево-вниз
    #     pochito.check_attak = False
    #     pochito.update([-1, 1], "left")

    #     updates(pygame, screen, pochito, zombies, ui, bloods)

    # elif keys[pygame.K_a]:
    #     # Движение в лево
    #     pochito.check_attak = False
    #     pochito.update([-1, 0], "left")

    #     updates(pygame, screen, pochito, zombies, ui, bloods)

    # elif keys[pygame.K_w]:
    #     # Движение вверх
    #     pochito.check_attak = False
    #     pochito.update([0, -1], pochito.direction)

    #     updates(pygame, screen, pochito, zombies, ui, bloods)

    # elif keys[pygame.K_d]:
    #     # Движение вправо
    #     pochito.check_attak = False
    #     pochito.update([1, 0], "right")

    #     updates(pygame, screen, pochito, zombies, ui, bloods)

    # elif keys[pygame.K_s]:
    #     # Движение вниз
    #     pochito.check_attak = False
    #     pochito.update([0, 1], pochito.direction)

    #     updates(pygame, screen, pochito, zombies, ui, bloods)

    # else:
    #     pochito.check_attak = False
    #     pochito.image_anim_count = 0
    #     if pochito.direction == "right_attak":
    #         pochito.update([0, 0], "right")
    #     elif pochito.direction == "left_attak":
    #         pochito.update([0, 0], "left")
    #     elif pochito.direction == "left":
    #         pochito.update([0, 0], "left")

    updates(pygame, screen, pochito, zombies, ui)


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
