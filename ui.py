import pygame


class UI(pygame.sprite.Sprite):
    """
		Класс отвечающий за весь UI игры
	"""

    def __init__(self, screen):
        super(UI, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()  # Получаем границы экрана
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height

        self.background = pygame.transform.scale(pygame.image.load("src/bg.png").convert_alpha(), (self.screen_width, self.screen_height))

        self.pochito_ico = pygame.transform.scale(pygame.image.load('src/pochito_ico.png').convert_alpha(), 
            (self.screen_width // 100 * 10, self.screen_width // 100 * 10))
        
        self.pochito_healf_array = [
            pygame.transform.scale(pygame.image.load("src/healf_1.png").convert_alpha(), 
            (self.screen_width // 100 * 20, self.screen_width // 100 * 20 // 2)),
            pygame.transform.scale(pygame.image.load("src/healf_2.png").convert_alpha(), 
            (self.screen_width // 100 * 20, self.screen_width // 100 * 20 // 2)),
            pygame.transform.scale(pygame.image.load("src/healf_3.png").convert_alpha(), 
            (self.screen_width // 100 * 20, self.screen_width // 100 * 20 // 2)),
            pygame.transform.scale(pygame.image.load("src/healf_4.png").convert_alpha(), 
            (self.screen_width // 100 * 20, self.screen_width // 100 * 20 // 2)),
            pygame.transform.scale(pygame.image.load("src/healf_5.png").convert_alpha(), 
            (self.screen_width // 100 * 20, self.screen_width // 100 * 20 // 2))
        ]

        self.shake_count = 0

    def drawing(self, healf):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.pochito_ico, (20, 20))  # Иконка почиты

        # Отображение Здоровья
        if 80 <= healf:
            # 80-100
            self.screen.blit(self.pochito_healf_array[4], (40 + self.screen_width // 100 * 10, 20))
        elif 60 <= healf < 80:
            # 60-80
            self.screen.blit(self.pochito_healf_array[3], (40 + self.screen_width // 100 * 10, 20))
        elif 40 <= healf < 60:
            # 40-60
            self.screen.blit(self.pochito_healf_array[2], (40 + self.screen_width // 100 * 10, 20))
        elif 20 <= healf < 40:
            # 20-40
            self.screen.blit(self.pochito_healf_array[1], (40 + self.screen_width // 100 * 10, 20))
        elif 0 <= healf < 20:
            # 0-20
            self.screen.blit(self.pochito_healf_array[0], (40 + self.screen_width // 100 * 10, 20))

    def shake_screen(self):
        if self.shake_count <= 4:

            if self.shake_count == 0:
                self.screen.scroll(2,2)

            elif self.shake_count == 1:
                self.screen.scroll(-4,-4)

            elif self.shake_count == 2:
                self.screen.scroll(0,-4)

            elif self.shake_count == 3:
                self.screen.scroll(4,4)

            elif self.shake_count == 4:
                self.screen.scroll(-2,-2)

            self.shake_count += 1
        else:
            self.shake_count = 0
        
