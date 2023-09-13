import random

from zombie import Zombie


def updates(pygame, screen, pochito, zombies, ui):
    # UI
    ui.drawing(pochito.health)

    # GAME
    pochito.drawing()

    # Проверка жизней каждого Зомби
    for zombie in zombies.sprites():
        if zombie.health <= 0:
            if pochito.health <= 100:  # Ограничение, что бы здоровья всегда было мало
                pochito.health += 50

            # Восстанавливаем зомби
            zombie.health = 100
            zombie.attak += 0.1
            zombie.direction_slop = random.choice([-1, 0, 1])
            pochito.kills_count += 1

            random_pos_x = [random.randint(-200, -100), random.randint(900, 1000)]
            zombie.x = random_pos_x[random.randint(0, 1)]
            zombie.y = random.randint(200, 400)

        # Атака зомби в случае соприкосновения с игроком
        if pochito.rect.colliderect(zombie.rect):
            pochito.health -= zombie.attak

    zombies.draw(screen)

    pygame.display.flip()


def controll(pygame, screen, pochito, zombies, ui):
    """
        Контролер, действия после нажатия определённых клавиш
    """
    keys = pygame.key.get_pressed()  # Получаем нажатые клавиши

    # Движение + Атака
    if keys[pygame.K_d] == True and keys[pygame.K_RIGHT] == True:
        # Движение вправо и атака
        for zombie in zombies.sprites():
            if pochito.rect.colliderect(zombie.rect):
                zombie.health -= pochito.attak

        pochito.check_attak = True
        pochito.update([1, 0], "right_attak")

        return

    elif keys[pygame.K_a] == True and keys[pygame.K_LEFT] == True:
        # Движение влево и атака
        for zombie in zombies.sprites():
            if pochito.rect.colliderect(zombie.rect):
                zombie.health -= pochito.attak

        pochito.check_attak = True
        pochito.update([-1, 0], "left_attak")

        return

    # Move
    if keys[pygame.K_a] == True and keys[pygame.K_w] == True:
        # Движение в лево-вверх
        pochito.check_attak = False
        pochito.update([-1, -1], "left")

        updates(pygame, screen, pochito, zombies, ui)

    elif keys[pygame.K_w] == True and keys[pygame.K_d] == True:
        # Движение вверх-право
        pochito.check_attak = False
        pochito.update([1, -1], "right")

        updates(pygame, screen, pochito, zombies, ui)

    elif keys[pygame.K_d] == True and keys[pygame.K_s] == True:
        # Движение в право-вниз
        pochito.check_attak = False
        pochito.update([1, 1], "right")

        updates(pygame, screen, pochito, zombies, ui)

    elif keys[pygame.K_s] == True and keys[pygame.K_a] == True:
        # Движение в лево-вниз
        pochito.check_attak = False
        pochito.update([-1, 1], "left")

        updates(pygame, screen, pochito, zombies, ui)

    if keys[pygame.K_a]:
        # Движение в лево
        pochito.check_attak = False
        pochito.update([-1, 0], "left")

        updates(pygame, screen, pochito, zombies, ui)

    elif keys[pygame.K_w]:
        # Движение вверх
        pochito.check_attak = False
        pochito.update([0, -1], pochito.direction)

        updates(pygame, screen, pochito, zombies, ui)

    elif keys[pygame.K_d]:
        # Движение вправо
        pochito.check_attak = False
        pochito.update([1, 0], "right")

        updates(pygame, screen, pochito, zombies, ui)

    elif keys[pygame.K_s]:
        # Движение вниз
        pochito.check_attak = False
        pochito.update([0, 1], pochito.direction)

        updates(pygame, screen, pochito, zombies, ui)

    else:
        pochito.check_attak = False
        pochito.image_anim_count = 0

        updates(pygame, screen, pochito, zombies, ui)


def create_zombie(screen, zombies, count_zombie: int):
    """
        Функция генерирует зомби в заданном колличестве `count_zombie`
    """
    for item in range(count_zombie):
        random_pos_x = [random.randint(-200, -100), random.randint(900, 1000)]

        pos_x = random_pos_x[random.randint(0, 1)]
        pos_y = random.randint(200, 400)

        # Создание и добавление зомби
        zombie = Zombie(screen, pos_x, pos_y)
        zombies.add(zombie)
