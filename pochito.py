import pygame


class Pochito(pygame.sprite.Sprite):
    """
        Класс отвечающий за почиту
    """

    def __init__(self, screen, x, y):
        super(Pochito, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()  # Получаем границы экрана
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height

        self.move_right = [
            pygame.transform.scale(pygame.image.load('src/pochito_right1.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/pochito_right2.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/pochito_right3.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/pochito_right4.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/pochito_right5.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/pochito_right6.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/pochito_right7.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/pochito_right8.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/pochito_right9.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/pochito_right10.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/pochito_right11.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10))
        ]
        self.move_right_attak = [
        	pygame.transform.scale(pygame.image.load('src/pochito_attak_right1.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10)),
            pygame.transform.scale(pygame.image.load('src/pochito_attak_right2.png').convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10))
        ]
        self.image_anim_count = 0

        self.image = self.move_right[0]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Переменные персонажа
        self.health = 100  # Здоровье
        self.attak_hit = 1  # Сила
        self.speed = 10  # Скорость
        self.direction = "right"
        self.check_attak = False  # Атакует ли Почито
        self.kills_count = 0  # Счётчик убийств
        self.status = {"move_x":False,"move_y":False,"hit":False} # Move, Attak

    def drawing(self):
        if self.health >= 1:

            if self.direction == "left":
                if self.status['hit']:
                    self.image = pygame.transform.flip(self.move_right_attak[self.image_anim_count], True, False)
                    self.screen.blit(self.image, (self.x, self.y,))
                else:
                    self.image = pygame.transform.flip(self.move_right[self.image_anim_count], True, False)
                    self.screen.blit(self.image, (self.x, self.y,))

            elif self.direction == "right":
                if self.status['hit']:
                    self.screen.blit(self.move_right_attak[self.image_anim_count], (self.x, self.y,))
                else:
                    self.screen.blit(self.move_right[self.image_anim_count], (self.x, self.y,))


    def update(self):
        if self.health >= 1:

            # Движение
            if self.rect.bottom < self.screen_rect.bottom: # Барьер снизу
                if self.rect.top > self.screen_height // 100 * 50: # Барьер сверху
                    if self.rect.right < self.screen_rect.right: # Барьер слева
                        if self.rect.left > self.screen_rect.left: # Барьер справа

                            if self.status['hit']:
                                if self.image_anim_count < len(self.move_right_attak) - 1:
                                    self.image_anim_count += 1
                                else:
                                    self.image_anim_count = 0

                            self.x += self.status["move_x"] * self.speed
                            self.y += self.status["move_y"] * self.speed
                        else:
                            self.x += 5
                            self.y += 0
                    else:
                        self.x -= 5
                        self.y += 0
                else:
                    self.x += 0
                    self.y += 5
            else:
                self.x += 0
                self.y -= 5

            self.rect.x = self.x
            self.rect.y = self.y
