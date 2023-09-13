import pygame


class Pochito(pygame.sprite.Sprite):
    """
        Класс отвечающий за почиту
    """

    def __init__(self, screen, x, y):
        super(Pochito, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()  # Получаем границы экрана

        self.move_right = [
            pygame.image.load('src/pochito_right1.png'),
            pygame.image.load('src/pochito_right2.png'),
            pygame.image.load('src/pochito_right3.png'),
            pygame.image.load('src/pochito_right4.png'),
            pygame.image.load('src/pochito_right5.png'),
            pygame.image.load('src/pochito_right6.png'),
            pygame.image.load('src/pochito_right7.png'),
            pygame.image.load('src/pochito_right8.png'),
            pygame.image.load('src/pochito_right9.png'),
            pygame.image.load('src/pochito_right10.png'),
            pygame.image.load('src/pochito_right11.png')
        ]
        self.move_right_attak = [
            pygame.image.load('src/pochito_attak_right1.png'),
            pygame.image.load('src/pochito_attak_right2.png')
        ]
        self.image_anim_count = 0
        self.direction = "right"

        self.image = self.move_right[0]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Переменные персонажа
        self.health = 100  # Здоровье
        self.attak = 1  # Сила
        self.speed = 5  # Скорость
        self.check_attak = False  # Атакует ли Почито
        self.kills_count = 0  # Счётчик убийств

    def drawing(self):
        if self.health >= 1:

            if self.direction == "left_attak":
                self.image = pygame.transform.flip(self.move_right_attak[self.image_anim_count], True, False)
                self.screen.blit(self.image, (self.x, self.y,))

            elif self.direction == "left":
                self.image = pygame.transform.flip(self.move_right[self.image_anim_count], True, False)
                self.screen.blit(self.image, (self.x, self.y,))

            elif self.direction == "right":
                self.screen.blit(self.move_right[self.image_anim_count], (self.x, self.y,))

            elif self.direction == "right_attak":
                self.screen.blit(self.move_right_attak[self.image_anim_count], (self.x, self.y,))

    def update(self, move: list, direction: str):
        if self.health >= 1:
            if self.direction != direction:
                self.image_anim_count = 0
            self.direction = direction

            if self.rect.bottom < self.screen_rect.bottom:
                if self.rect.top > self.screen_rect.top + 200:
                    if self.rect.right < self.screen_rect.right:
                        if self.rect.left > self.screen_rect.left:

                            if self.direction == "left_attak" or self.direction == "right_attak":
                                if self.image_anim_count < len(self.move_right_attak) - 1:
                                    self.image_anim_count += 1
                                else:
                                    self.image_anim_count = 0

                            elif self.direction == "left" or self.direction == "right":
                                if self.image_anim_count < len(self.move_right) - 1:
                                    self.image_anim_count += 1
                                else:
                                    self.image_anim_count = 0

                            self.x += move[0] * self.speed
                            self.y += move[1] * self.speed
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
