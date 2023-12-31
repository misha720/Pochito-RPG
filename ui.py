import pygame
import time
import os

import controll as ctrl


class UI(pygame.sprite.Sprite):
    """
		Класс отвечающий за весь UI игры
	"""

    def __init__(self, screen, start_round, pochito):
        super(UI, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()  # Получаем границы экрана
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        self.pochito = pochito

        # Clock
        self.start_round = start_round # Время начала игры
        self.round_game = 0 # Какой раунд сейчас в игре
        self.clock = time.time() - self.start_round # Секунд прошло с начала игры
        self.minute_since_past_round = self.clock // 60

        # Font
        pygame.font.init()
        self.font_family = pygame.font.match_font("ubuntu")

        # Background
        self.background = pygame.transform.scale(pygame.image.load("src/bg.png").convert_alpha(), (self.screen_width, self.screen_height))

        # Pochito Icon
        self.pochito_ico = pygame.transform.scale(pygame.image.load('src/pochito_ico.png').convert_alpha(), 
            (self.screen_width // 100 * 10, self.screen_width // 100 * 10))
        
        # Pochito Healf
        self.pochito_healf_frames = []
        for frame_path in sorted(os.listdir('src/ui/health/')):
            frame_path = "src/ui/health/" + frame_path
            frame = pygame.transform.scale(pygame.image.load(frame_path).convert_alpha(), 
                (self.screen_width // 100 * 20, self.screen_width // 100 * 4))
            self.pochito_healf_frames.append(frame)

        # Pochito Energy
        self.pochito_energy_frames = []
        for frame_path in sorted(os.listdir('src/ui/energy/')):
            frame_path = "src/ui/energy/" + frame_path
            frame = pygame.transform.scale(pygame.image.load(frame_path).convert_alpha(), 
                (self.screen_width // 100 * 20, self.screen_width // 100 * 4))
            self.pochito_energy_frames.append(frame)

        # Signal Icon
        self.is_signed_worked = False
        self.signal_count = 0
        self.signal_frame = pygame.transform.scale(pygame.image.load("src/signal.png").convert_alpha(), 
            (self.screen_width // 100 * 10, self.screen_width // 100 * 10))
        self.signal_frame_rect = self.signal_frame.get_rect()

        # Shake Screen
        self.shake_count = 0

    def drawing(self):
        ui_command = ""
        self.screen.blit(self.background, (0, 0))
        
        if self.pochito.is_alive():

            # Pochito Icon
            self.screen.blit(self.pochito_ico, (20, 20))  # Иконка почиты

            # Round Controll
            self.clock = time.time() - self.start_round # Секунд прошло с начала игры
            self.minute_since_past_round = self.clock // 60
            
            # Clock Game
            Font = pygame.font.Font(self.font_family, 60)
            text = Font.render(str( time.strftime("%M:%S",time.localtime(self.clock)) ), 1, (255, 255, 255))
            self.screen.blit(text,(self.screen_width // 2 - text.get_rect().width // 2, 20))

            # Draw Health
            if self.pochito.health >= 100:
                # 100+
                self.screen.blit(self.pochito_healf_frames[0], 
                    (20 + self.pochito_ico.get_rect().width + 20, 20))

            elif 80 <= self.pochito.health < 100:
                # 80-100
                self.screen.blit(self.pochito_healf_frames[1], 
                    (20 + self.pochito_ico.get_rect().width + 20, 20))
            
            elif 60 <= self.pochito.health < 80:
                # 60-80
                self.screen.blit(self.pochito_healf_frames[2], 
                    (20 + self.pochito_ico.get_rect().width + 20, 20))
            
            elif 40 <= self.pochito.health < 60:
                # 40-60
                self.screen.blit(self.pochito_healf_frames[3], 
                    (20 + self.pochito_ico.get_rect().width + 20, 20))
            
            elif 20 <= self.pochito.health < 40:
                # 20-40
                self.screen.blit(self.pochito_healf_frames[4], 
                    (20 + self.pochito_ico.get_rect().width + 20, 20))
            
            elif self.pochito.health < 20:
                # 0-20
                self.screen.blit(self.pochito_healf_frames[5], 
                    (20 + self.pochito_ico.get_rect().width + 20, 20))

            # Draw Energy
            if self.pochito.energy >= 100:
                # 100+
                self.screen.blit(self.pochito_energy_frames[0], 
                    (20 + self.pochito_ico.get_rect().width + 20,
                     20 + self.pochito_healf_frames[0].get_rect().height + 10))

            elif 80 <= self.pochito.energy < 100:
                # 80-100
                self.screen.blit(self.pochito_energy_frames[1], 
                    (20 + self.pochito_ico.get_rect().width + 20,
                     20 + self.pochito_healf_frames[0].get_rect().height + 10))
            
            elif 60 <= self.pochito.energy < 80:
                # 60-80
                self.screen.blit(self.pochito_energy_frames[2], 
                    (20 + self.pochito_ico.get_rect().width + 20,
                     20 + self.pochito_healf_frames[0].get_rect().height + 10))
            
            elif 40 <= self.pochito.energy < 60:
                # 40-60
                self.screen.blit(self.pochito_energy_frames[3], 
                    (20 + self.pochito_ico.get_rect().width + 20,
                     20 + self.pochito_healf_frames[0].get_rect().height + 10))
            
            elif 20 <= self.pochito.energy < 40:
                # 20-40
                self.screen.blit(self.pochito_energy_frames[4], 
                    (20 + self.pochito_ico.get_rect().width + 20,
                     20 + self.pochito_healf_frames[0].get_rect().height + 10))
            
            elif 0 < int(self.pochito.energy) < 20 :
                # 0-20
                self.screen.blit(self.pochito_energy_frames[5], 
                    (20 + self.pochito_ico.get_rect().width + 20,
                     20 + self.pochito_healf_frames[0].get_rect().height + 10))

            elif int(self.pochito.energy) <= 0:
                # 0
                self.screen.blit(self.pochito_energy_frames[6], 
                    (20 + self.pochito_ico.get_rect().width + 20,
                     20 + self.pochito_healf_frames[0].get_rect().height + 10))

            # Signal
            if self.is_signed_worked:
                self.signal_count += 1

                if 0 <= self.signal_count <= 25:
                    self.screen.blit(self.signal_frame, (self.screen_width // 2 - self.signal_frame_rect.width // 2,
                     self.screen_height // 2 - self.signal_frame_rect.height // 2))

                elif 50 <= self.signal_count <= 75:
                    self.screen.blit(self.signal_frame, (self.screen_width // 2 - self.signal_frame_rect.width // 2,
                     self.screen_height // 2 - self.signal_frame_rect.height // 2))

                elif 100 <= self.signal_count <= 125:
                    self.screen.blit(self.signal_frame, (self.screen_width // 2 - self.signal_frame_rect.width // 2,
                     self.screen_height // 2 - self.signal_frame_rect.height // 2))

                elif 150 <= self.signal_count <= 175:
                    self.screen.blit(self.signal_frame, (self.screen_width // 2 - self.signal_frame_rect.width // 2,
                     self.screen_height // 2 - self.signal_frame_rect.height // 2))

                elif 200 <= self.signal_count <= 225:
                    self.screen.blit(self.signal_frame, (self.screen_width // 2 - self.signal_frame_rect.width // 2,
                     self.screen_height // 2 - self.signal_frame_rect.height // 2))

                elif 250 <= self.signal_count <= 275:
                    self.screen.blit(self.signal_frame, (self.screen_width // 2 - self.signal_frame_rect.width // 2,
                     self.screen_height // 2 - self.signal_frame_rect.height // 2))

                elif self.signal_count > 275:
                    self.is_signed_worked = False



        else:
            Font = pygame.font.Font(self.font_family, 50)
            Font2 = pygame.font.Font(self.font_family, 40)
            text = Font.render("You Die", 1, (255, 0, 0))
            text_count = Font2.render("Count - " + str(self.pochito.kills_count), 1, (255, 0, 0))
            self.screen.blit(text, (self.screen_width // 2 - text.get_width(), self.screen_height // 2 - text.get_height() - text_count.get_height() - 20))
            self.screen.blit(text_count, ( self.screen_width // 2 - text_count.get_width(), self.screen_height // 2 - text_count.get_height()))

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
        
