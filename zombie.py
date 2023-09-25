import pygame
import random


class Zombie(pygame.sprite.Sprite):
    """
		Класс отвечающий за каждого зомби
	"""

    def __init__(self, screen, x, y):
        super(Zombie, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()  # Получаем границы экрана
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height

        self.move_right = [
            pygame.transform.scale(pygame.image.load('src/zombi1.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/zombi2.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/zombi3.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/zombi4.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/zombi5.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/zombi6.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/zombi7.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/zombi8.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/zombi9.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/zombi10.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/zombi11.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/zombi12.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10))
        ]
        self.image_anim_count = 0
        self.takt = 0 # От 0 до 3 кадров

        self.image = self.move_right[self.image_anim_count]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Zombie Varaible
        self.health = 100
        self.attak = 1
        self.speed = 1
        self.direction_slop = random.choice([-1, 0, 1])  # Направление куда будет постоянно уклоняться зомби
        self.direction_move = "right"  # Направление куда будет поворачиваться зомби
        self.first_contact = 0 # При соприкосновении с почито, запишется время

    def update(self, pochito_pos, pochito_check_attak):
        if self.image_anim_count < len(self.move_right) - 1:
            self.takt += 1
            if self.takt == 2:
                self.image_anim_count += 1
                self.takt = 0
        else:
            self.image_anim_count = 0

        # Moved
        if self.rect.bottom < self.screen_rect.bottom:
            if self.rect.top > self.screen_height // 100 * 50:
                if pochito_check_attak:
                    # Если Почито сейчас атакует то нужно всех зомби убрать с его пути

                    # Проверяем, может ли нас атаковать Почито
                    # Уходим только из под удара

                    if self.rect.y in range(int(pochito_pos[1]), int(pochito_pos[1]) + 100):
                        self.y += self.direction_slop * self.speed
                    
                    else:
                        if self.rect.y > pochito_pos[1]:
                            # Зомби выше
                            self.y -= 1 * self.speed

                        else:
                            # Зомби ниже
                            self.y += 1 * self.speed

                    if self.rect.x > pochito_pos[0]:
                        # Зомби с права
                        self.x -= 1 * self.speed

                    else:
                        # Зомби с лева
                        self.x += 1 * self.speed
                else:

                    if self.rect.x > pochito_pos[0]:
                        # Зомби с права
                        self.x -= 1 * self.speed

                    else:
                        # Зомби с лева
                        self.x += 1 * self.speed

                    if self.rect.y > pochito_pos[1]:
                        # Зомби выше
                        self.y -= 1 * self.speed

                    else:
                        # Зомби ниже
                        self.y += 1 * self.speed

            else:
                self.x += 0
                self.y += 5
        else:
            self.x += 0
            self.y -= 5

        self.rect.x = self.x
        self.rect.y = self.y

        # Direction Move
        if self.rect.x > pochito_pos[0]:
            # Зомби с права
            self.image = pygame.transform.flip(self.move_right[self.image_anim_count], True, False)

        else:
            # Зомби с лева
            self.image = pygame.transform.flip(self.move_right[self.image_anim_count], False, False)
