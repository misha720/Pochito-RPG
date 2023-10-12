import pygame
import random
import os


class ZombieDemon(pygame.sprite.Sprite):
    """
		Класс отвечающий за каждого зомби
	"""

    def __init__(self, screen, x, y):
        super(ZombieDemon, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()  # Получаем границы экрана
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height

        # ZD move
        self.move_frames = []
        for frame_path in os.listdir('src/ZombieDemon/move'):
            frame_path = "src/ZombieDemon/move/" + frame_path
            frame = pygame.transform.scale(pygame.image.load(frame_path).convert_alpha(), 
                (self.screen_width // 100 * 15, self.screen_width // 100 * 10))
            self.move_frames.append(frame)

        # ZD attak
        self.attak_frames = []
        for frame_path in os.listdir('src/ZombieDemon/attak'):
            frame_path = "src/ZombieDemon/attak/" + frame_path
            frame = pygame.transform.scale(pygame.image.load(frame_path).convert_alpha(), 
                (self.screen_width // 100 * 15, self.screen_width // 100 * 10))
            self.attak_frames.append(frame)

        

        # ZD die
        # self.move_frames = []
        # for frame_path in os.listdir('src/ZombieDemon/move'):
        #     frame_path = "src/pochito/move/" + frame_path
        #     frame = pygame.transform.scale(pygame.image.load(frame_path).convert_alpha(), 
        #         (self.screen_width // 100 * 15, self.screen_width // 100 * 10))
        #     self.move_frames.append(frame)

        # Image
        self.count_frame_move = 0
        self.count_frame_attak = 0
        self.delay_move = 0 # Сколько приходиться кадров на один фрейм
        self.delay_attak = 0 # Сколько приходиться кадров на один фрейм
        self.image = self.move_frames[0]
        self.rect = self.image.get_rect()
        self.size = [self.rect.width, self.rect.height]
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        

        # ZD Varaible
        self.health = 1000
        self.attak = 1
        self.speed = 1
        self.direction = "right"  # Направление куда будет поворачиваться зомби
        self.status = 'move' # Move, Attak, Die
        self.called = False
        self.time_called = 0
        self.is_used_weapon = False
        self.positions_pochito = []
        self.positions_boss = [
            [self.screen_width // 100 * 50, self.screen_height // 100 * 70],
            [self.screen_width // 100 * 20, self.screen_height // 100 * 50],
            [self.screen_width // 100 * 70, self.screen_height // 100 * 50]
        ] # Позиции где Босс будет находиться
        self.random_pos_boss = random.randint(0,2)


    def drawing(self):
        if self.called:
            if self.health >= 1:

                if self.direction == "left":
                    if self.status == "attak":
                        self.image = pygame.transform.flip(self.attak_frames[self.count_frame_attak], True, False)
                        self.screen.blit(self.image, (self.x, self.y,))
                        
                    else:
                        self.image = pygame.transform.flip(self.move_frames[self.count_frame_move], True, False)
                        self.screen.blit(self.image, (self.x, self.y,))

                elif self.direction == "right":
                    if self.status == "attak":
                        self.screen.blit(self.attak_frames[self.count_frame_attak], (self.x, self.y,))
                    
                    else:
                        self.screen.blit(self.move_frames[self.count_frame_move], (self.x, self.y,))


    def update(self, pochito_pos):
        if self.called:
            if self.is_alive():

                # Controll Attak
                if self.status == "attak":
                    # Запрещаем двигаться
                    self.rect.x = self.x
                    self.rect.y = self.y

                    # Animation
                    if self.count_frame_attak < len(self.attak_frames) - 1:
                        self.delay_attak += 1
                        self.positions_pochito.append(pochito_pos)
                        if self.delay_attak > 10:
                            self.count_frame_attak += 1
                            self.delay_attak = 0

                    if self.count_frame_attak == 6 and self.is_used_weapon == False:
                        
                        # Запустить weapon
                        self.is_used_weapon = True

                else:
                    # Движение
                    if self.rect.bottom < self.screen_rect.bottom: # Барьер снизу
                        if self.rect.top > self.screen_height // 100 * 40: # Барьер сверху
                            if self.rect.right < self.screen_rect.right: # Барьер слева
                                if self.rect.left > self.screen_rect.left: # Барьер справа
                                    
                                    # Animation
                                    if self.count_frame_move < len(self.move_frames) - 1:
                                        self.delay_move += 1
                                        if self.delay_move > 10:
                                            self.count_frame_move += 1
                                            self.delay_move = 0
                                    else:
                                        self.count_frame_move = 0

                                    # Moved to Center Screen
                                    if self.rect.x > self.positions_boss[self.random_pos_boss][0]:
                                        # Зомби с права
                                        self.x -= 1 * self.speed

                                    else:
                                        # Зомби с лева
                                        self.x += 1 * self.speed

                                    if self.rect.y > self.positions_boss[self.random_pos_boss][1]:
                                        # Зомби выше
                                        self.y -= 1 * self.speed

                                    else:
                                        # Зомби ниже
                                        self.y += 1 * self.speed

                                else:
                                    self.x += 10
                                    self.y += 0
                            else:
                                self.x -= 10
                                self.y += 0
                        else:
                            self.x += 0
                            self.y += 10
                    else:
                        self.x += 0
                        self.y -= 10

                self.rect.x = self.x
                self.rect.y = self.y


    def is_alive(self):
        """
            Check pochito is alive
        """
        if self.health <= 0:
            self.alive == False
            return False
        else:
            self.alive == True
            return True