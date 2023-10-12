import pygame
import random
import os


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

        # Zombie Move
        self.move_frames = []
        for frame_path in os.listdir('src/zombie/move/'):
            frame_path = "src/zombie/move/" + frame_path
            frame = pygame.transform.scale(pygame.image.load(frame_path).convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10))
            self.move_frames.append(frame)

        # Zombie Attak
        self.attak_frames = []
        for frame_path in os.listdir('src/zombie/attak/'):
            frame_path = "src/zombie/attak/" + frame_path
            frame = pygame.transform.scale(pygame.image.load(frame_path).convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10))
            self.attak_frames.append(frame)
        
        # Zombie Die
        self.die_frames = []
        for frame_path in os.listdir('src/zombie/die/'):
            frame_path = "src/zombie/die/" + frame_path
            frame = pygame.transform.scale(pygame.image.load(frame_path).convert_alpha(), 
                (self.screen_width // 100 * 10, self.screen_width // 100 * 10))
            self.die_frames.append(frame)

        # Image
        self.count_frame_move = 0
        self.count_frame_attak = 0
        self.count_frame_die = 0
        self.delay_move = 0
        self.delay_attak = 0
        self.delay_die = 0
        self.image = self.move_frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Zombie Varaible
        self.health = 100
        self.attak = 1
        self.speed = 1
        self.direction_slop = random.choice([-1,0,1])  # Направление куда будет постоянно уклоняться зомби
        self.direction_move = "right"  # Направление куда будет поворачиваться зомби
        self.first_contact = 0 # При соприкосновении с почито, запишется время
        self.status = 'move' # Move, Attak, Die

    def update(self, pochito_pos, pochito_check_attak, pochito_size):
        if self.status == "move":
            if self.count_frame_move < len(self.move_frames) - 1:
                self.delay_move += 1
                if self.delay_move == 10:
                    self.count_frame_move += 1
                    self.delay_move = 0
            else:
                self.count_frame_move = 0

        elif self.status == "attak":
            if self.count_frame_attak < len(self.attak_frames) - 1:
                self.delay_attak += 1
                if self.delay_attak == 10:
                    self.count_frame_attak += 1
                    self.delay_attak = 0
            else:
                self.count_frame_attak = 0

        elif self.status == "die":
            if self.count_frame_die < len(self.die_frames) - 1:
                self.delay_die += 1
                if self.delay_die == 10:
                    self.count_frame_die += 1
                    self.delay_die = 0
            else:
                self.count_frame_die = 0

        # Moved
        if self.status == "die":
            if self.direction_move == "right":
                self.image = self.die_frames[self.count_frame_die]
            else:
                self.image = pygame.transform.flip(self.die_frames[self.count_frame_die], True, False)
        else:
            if self.rect.bottom < self.screen_rect.bottom:
                if self.rect.top > self.screen_height // 100 * 40:
                    if pochito_check_attak:
                        # Если Почито сейчас атакует то нужно всех зомби убрать с его пути

                        # Проверяем, может ли нас атаковать Почито
                        # Уходим только из под удара

                        if self.rect.y in range(int(pochito_pos[1]) - pochito_size[1], int(pochito_pos[1]) + pochito_size[1]):
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
            if self.status == "move":
                if self.rect.x > pochito_pos[0]:
                    # Зомби с права
                    self.image = pygame.transform.flip(self.move_frames[self.count_frame_move], True, False)

                else:
                    # Зомби с лева
                    self.image = pygame.transform.flip(self.move_frames[self.count_frame_move], False, False)
            
            elif self.status == "attak":

                if self.rect.x > pochito_pos[0]:
                    # Зомби с права
                    self.image = pygame.transform.flip(self.attak_frames[self.count_frame_attak], True, False)
                else:
                    # Зомби с лева
                    self.image = pygame.transform.flip(self.attak_frames[self.count_frame_attak], False, False)          
        
        

                