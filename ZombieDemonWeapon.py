import pygame
import random
from math import atan2, degrees, pi
import time

class ZombieDemonWeapon(pygame.sprite.Sprite):
    """
        Класс отвечающий за каждого зомби
    """

    def __init__(self, screen):
        super(ZombieDemonWeapon, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()  # Получаем границы экрана
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height

        # ZD weapon
        self.weapon_frames = [
            pygame.transform.scale(pygame.image.load('src/ZombieDemon/weapon/001.png').convert_alpha(), 
                (self.screen_width // 100 * 2, self.screen_width // 100 * 2)),
            pygame.transform.scale(pygame.image.load('src/ZombieDemon/weapon/002.png').convert_alpha(), 
                (self.screen_width // 100 * 2, self.screen_width // 100 * 2)),
            pygame.transform.scale(pygame.image.load('src/ZombieDemon/weapon/003.png').convert_alpha(), 
                (self.screen_width // 100 * 2, self.screen_width // 100 * 2)),
            pygame.transform.scale(pygame.image.load('src/ZombieDemon/weapon/004.png').convert_alpha(), 
                (self.screen_width // 100 * 2, self.screen_width // 100 * 2)),
            pygame.transform.scale(pygame.image.load('src/ZombieDemon/weapon/005.png').convert_alpha(), 
                (self.screen_width // 100 * 2, self.screen_width // 100 * 2)),
            pygame.transform.scale(pygame.image.load('src/ZombieDemon/weapon/006.png').convert_alpha(), 
                (self.screen_width // 100 * 2, self.screen_width // 100 * 2)),
            pygame.transform.scale(pygame.image.load('src/ZombieDemon/weapon/007.png').convert_alpha(), 
                (self.screen_width, self.screen_width // 100 * 2)),
            pygame.transform.scale(pygame.image.load('src/ZombieDemon/weapon/008.png').convert_alpha(), 
                (self.screen_width, self.screen_width // 100 * 2)),
            pygame.transform.scale(pygame.image.load('src/ZombieDemon/weapon/009.png').convert_alpha(), 
                (self.screen_width, self.screen_width // 100 * 2)),
            pygame.transform.scale(pygame.image.load('src/ZombieDemon/weapon/010.png').convert_alpha(), 
                (self.screen_width, self.screen_width // 100 * 2)),
            pygame.transform.scale(pygame.image.load('src/ZombieDemon/weapon/011.png').convert_alpha(), 
                (self.screen_width, self.screen_width // 100 * 2)),
            pygame.transform.scale(pygame.image.load('src/ZombieDemon/weapon/012.png').convert_alpha(), 
                (self.screen_width, self.screen_width // 100 * 2))
        ]

        # Animator
        self.animator_worker = False
        self.time_start_animation = 0 #Время начала анимации
        self.speed_animation = 200 # Время в секундах

        self.delay_weapon = 0 # Сколько приходиться кадров на один фрейм
        self.count_frame_weapon = 0

        # Weapon
        self.weapon_image = self.weapon_frames[0]
        self.weapon_rect = self.weapon_image.get_rect()
        self.weapon_pos = [self.weapon_rect.x, self.weapon_rect.y]
        self.weapon_size = [self.weapon_rect.width, self.weapon_rect.height]
        self.is_used_weapon = False
        self.time_last_shot = 0 # Время последнего выстрела
        self.zombie_demon_rect: any
        self.pochito_pos = []

        self.point_attak = 0 # Градус что бы достич почито лучом ZD
        self.index_for_list_agree = 0 # Индекс в списке
        self.takt = 0

        # Line
        self.line_start_pos = []
        self.line_end_pos = []
        self.line_size = []
        
        

    def drawing(self):
        # Draw Weapon
        if self.is_used_weapon:
            # pygame.draw.line(self.screen,
            #     (255,0,0,255),
            #     self.line_start_pos,
            #     self.line_end_pos,
            # ) Включи для теста луча который на самом деле касается почито

            self.screen.blit(self.weapon_image, 
                self.weapon_pos)


    def update(self, ZombieDemon):
        self.is_used_weapon = ZombieDemon.is_used_weapon
        

        self.zombie_demon_rect = ZombieDemon.rect
        self.weapon_pos = [ZombieDemon.x + self.zombie_demon_rect.width // 2,
        ZombieDemon.y + self.zombie_demon_rect.height // 2]
        self.weapon_rect.x = self.weapon_pos[0]
        self.weapon_rect.y = self.weapon_pos[1]

        if self.is_used_weapon:

            self.point_attak = self.get_degree(ZombieDemon.positions_pochito)

            self.weapon_image = pygame.transform.rotate(self.weapon_frames[self.count_frame_weapon],
                self.point_attak)

            self.weapon_size = [self.weapon_image.get_rect().width,
                self.weapon_image.get_rect().height]
            self.line_size = [self.weapon_image.get_rect().width,
                self.weapon_image.get_rect().height]

            if self.point_attak > 360:
                self.point_attak // 360

            if 0 < self.point_attak < 90:
                # top-right
                self.weapon_pos[1] -= self.weapon_size[1]

                self.line_start_pos = [self.weapon_pos[0], self.weapon_pos[1] + self.weapon_size[1]]
                self.line_end_pos = [self.weapon_pos[0] + self.weapon_size[0], self.weapon_pos[1]]

            elif 90 < self.point_attak < 180:
                # left-top
                self.weapon_pos[0] -= self.weapon_size[0]
                self.weapon_pos[1] -= self.weapon_size[1]

                self.line_start_pos = [self.weapon_pos[0] + self.weapon_size[0], self.weapon_pos[1] + self.weapon_size[1]]
                self.line_end_pos = [self.weapon_pos[0], self.weapon_pos[1]]
                
            elif 180 < self.point_attak < 270:
                # bottom-left
                self.weapon_pos[0] -= self.weapon_size[0]

                self.line_start_pos = [self.weapon_pos[0] + self.weapon_size[0], self.weapon_pos[1]]
                self.line_end_pos = [self.weapon_pos[0], self.weapon_pos[1] + self.weapon_size[1]]
                
            elif 270 < self.point_attak < 360:
                # right-bottom
                self.line_start_pos = [self.weapon_pos[0], self.weapon_pos[1]]
                self.line_end_pos = [self.weapon_pos[0] + self.weapon_size[0], self.weapon_pos[1] + self.weapon_size[1]]
            
            self.weapon_rect.x = self.weapon_pos[0]
            self.weapon_rect.y = self.weapon_pos[1]
            self.weapon_rect.width = self.weapon_size[0]
            self.weapon_rect.height = self.weapon_size[1]

            if self.animator():
                ...
            else:

                # Останавливаем атаку по её завершению
                self.animator_worker = False
                self.count_frame_weapon = 0
                ZombieDemon.count_frame_attak = 0
                ZombieDemon.status = 'move'
                ZombieDemon.random_pos_boss = random.randint(0,2)
                ZombieDemon.positions_pochito.clear()
                self.is_used_weapon = False
                ZombieDemon.is_used_weapon = False
                

            

    def get_degree(self, list_point):
        # Вычисляет градус атаки

        if self.index_for_list_agree < len(list_point)-1:
            self.takt += 1

            if self.takt > 1:
                self.index_for_list_agree += 1
                self.takt = 0

        dx = list_point[self.index_for_list_agree][0] - self.weapon_pos[0]
        dy = list_point[self.index_for_list_agree][1] - self.weapon_pos[1]
        rads = atan2(-dy,dx)
        rads %= 2*pi
        return float(degrees(rads))

    def animator(self):
        if self.animator_worker == False:
            self.animator_worker = True
            self.time_start_animation = time.time()

        if self.count_frame_weapon < len(self.weapon_frames) - 1:
            past_time = (time.time() - self.time_start_animation) * 1000
            self.count_frame_weapon = int(past_time // self.speed_animation)

            return True
        else:
            return False