import pygame


class Blood(pygame.sprite.Sprite):
    """
		Класс отвечающий за поведение крови на карте
	"""

    def __init__(self, screen, x, y, start_time):
        super(Blood, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()  # Получаем границы экрана
        
        self.image = pygame.image.load('src/blood.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.start_time = start_time
        self.end_time = self.start_time + 5