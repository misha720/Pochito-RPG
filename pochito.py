import pygame
import os
import time


class Pochito(pygame.sprite.Sprite):
    """
        Класс отвечающий за почиту
    """

    def __init__(self, screen, position):
        super(Pochito, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()  # Получаем границы экрана
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height

        # Pochito Move
        self.move_frames = []
        for frame_path in sorted(os.listdir('src/pochito/move')):
            frame_path = "src/pochito/move/" + frame_path
            frame = pygame.transform.scale(pygame.image.load(frame_path).convert_alpha(), 
                (self.screen_width // 100 * 15, self.screen_width // 100 * 10))
            self.move_frames.append(frame)
            
        # Pochito Hit
        self.hit_frames = []
        for frame_path in sorted(os.listdir('src/pochito/hit')):
            frame_path = "src/pochito/hit/" + frame_path
            frame = pygame.transform.scale(pygame.image.load(frame_path).convert_alpha(), 
                (self.screen_width // 100 * 15, self.screen_width // 100 * 10))
            self.hit_frames.append(frame)
        
        # Pochito Super Hit
        self.super_hit_frames = []
        for frame_path in sorted(os.listdir('src/pochito/super_hit')):
            frame_path = "src/pochito/super_hit/" + frame_path
            frame = pygame.transform.scale(pygame.image.load(frame_path).convert_alpha(), 
                (self.screen_width // 100 * 15, self.screen_width // 100 * 10))
            self.super_hit_frames.append(frame)

        # Image
        self.count_frame_move = 0
        self.count_frame_hit = 0
        self.count_frame_super = 0
        self.delay_move = 0
        self.delay_hit = 0
        self.delay_super = 0
        self.image = self.move_frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Переменные персонажа
        self.health = 100  # Здоровье
        self.attak_hit = 0.5  # Сила
        self.attak_super_hit = 3  # Сила
        self.speed = 1  # Скорость
        self.direction = "right"
        self.check_attak = False  # Атакует ли Почито
        self.kills_count = 0  # Счётчик убийств
        self.status = {"move_x":0,"move_y":0,"hit":False, "super":False} # Move, Attak
        self.alive = True

    def drawing(self):
        if self.health >= 1:

            if self.direction == "left":
                if self.status['hit']:
                    self.image = pygame.transform.flip(self.hit_frames[self.count_frame_hit], True, False)
                    self.screen.blit(self.image, (self.x, self.y,))

                elif self.status['super']:
                    self.image = pygame.transform.flip(self.super_hit_frames[self.count_frame_super], True, False)
                    self.screen.blit(self.image, (self.x, self.y,))
                
                else:
                    self.image = pygame.transform.flip(self.move_frames[self.count_frame_move], True, False)
                    self.screen.blit(self.image, (self.x, self.y,))

            elif self.direction == "right":
                if self.status['hit']:
                    self.screen.blit(self.hit_frames[self.count_frame_hit], (self.x, self.y,))

                elif self.status['super']:
                    self.screen.blit(self.super_hit_frames[self.count_frame_super], (self.x, self.y,))
                
                else:
                    self.screen.blit(self.move_frames[self.count_frame_move], (self.x, self.y,))


    def update(self, FPS):
        if self.is_alive():
            self.speed = FPS // 20

            # Движение
            if self.rect.bottom < self.screen_rect.bottom: # Барьер снизу
                if self.rect.top > self.screen_height // 100 * 40: # Барьер сверху
                    if self.rect.right < self.screen_rect.right: # Барьер слева
                        if self.rect.left > self.screen_rect.left: # Барьер справа

                            if self.status['hit']:
                                if self.count_frame_hit < len(self.hit_frames) - 1:
                                    self.delay_hit += 1
                                    if self.delay_hit > 10:
                                        self.count_frame_hit += 1
                                        self.delay_hit = 0
                                else:
                                    self.count_frame_hit = 0

                            if self.status['super']:
                                if self.count_frame_super < len(self.super_hit_frames) - 1:
                                    self.delay_super += 1
                                    if self.delay_super > 10:
                                        self.count_frame_super += 1
                                        self.delay_super = 0
                                else:
                                    self.count_frame_super = 0

                            if self.status['move_x'] != 0 or self.status['move_y'] != 0:
                                if self.count_frame_move < len(self.move_frames) - 1:
                                    self.delay_move += 1
                                    if self.delay_move > 10:
                                        self.count_frame_move += 1
                                        self.delay_move = 0
                                else:
                                    self.count_frame_move = 0

                            self.x += self.status["move_x"] * self.speed
                            self.y += self.status["move_y"] * self.speed
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