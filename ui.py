import pygame


class UI(pygame.sprite.Sprite):
    """
		Класс отвечающий за весь UI игры
	"""

    def __init__(self, screen):
        super(UI, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()  # Получаем границы экрана
        self.pochito_ico = pygame.image.load('src/pochito_ico.png')
        self.pochito_healf_array = [
            pygame.image.load("src/healf_0.png"),
            pygame.image.load("src/healf_1.png"),
            pygame.image.load("src/healf_2.png"),
            pygame.image.load("src/healf_3.png"),
            pygame.image.load("src/healf_4.png"),
            pygame.image.load("src/healf_5.png")
        ]

    def drawing(self, healf):
        self.screen.blit(pygame.image.load("src/bg.png"), (0, 0))  # Задний фон
        self.screen.blit(self.pochito_ico, (10, 10))  # Иконка почиты

        # Отображение Здоровья
        if 80 <= healf:
            # 80-100
            self.screen.blit(self.pochito_healf_array[5], (120, 10))
        elif 60 <= healf < 80:
            # 60-80
            self.screen.blit(self.pochito_healf_array[4], (120, 10))
        elif 40 <= healf < 60:
            # 40-60
            self.screen.blit(self.pochito_healf_array[3], (120, 10))
        elif 20 <= healf < 40:
            # 20-40
            self.screen.blit(self.pochito_healf_array[2], (120, 10))
        elif 0 <= healf < 20:
            # 75-100
            self.screen.blit(self.pochito_healf_array[1], (120, 10))
