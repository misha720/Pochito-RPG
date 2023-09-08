import pygame
import random

class Zombie(pygame.sprite.Sprite):
	'''Класс Zombie'''
	def __init__(self, screen, x, y):
		super(Zombie,self).__init__()
		self.screen = screen
		self.screen_rect = self.screen.get_rect() # Получаем границы экрана

		self.move_right = [
			pygame.image.load('src/zombi1.png'),
			pygame.image.load('src/zombi1.png'),
			pygame.image.load('src/zombi1.png'),

			pygame.image.load('src/zombi2.png'),
			pygame.image.load('src/zombi2.png'),
			pygame.image.load('src/zombi2.png'),

			pygame.image.load('src/zombi3.png'),
			pygame.image.load('src/zombi3.png'),
			pygame.image.load('src/zombi3.png'),

			pygame.image.load('src/zombi4.png'),
			pygame.image.load('src/zombi4.png'),
			pygame.image.load('src/zombi4.png'),

			pygame.image.load('src/zombi5.png'),
			pygame.image.load('src/zombi5.png'),
			pygame.image.load('src/zombi5.png'),

			pygame.image.load('src/zombi6.png'),
			pygame.image.load('src/zombi6.png'),
			pygame.image.load('src/zombi6.png'),

			pygame.image.load('src/zombi7.png'),
			pygame.image.load('src/zombi7.png'),
			pygame.image.load('src/zombi7.png'),

			pygame.image.load('src/zombi8.png'),
			pygame.image.load('src/zombi8.png'),
			pygame.image.load('src/zombi8.png'),

			pygame.image.load('src/zombi9.png'),
			pygame.image.load('src/zombi9.png'),
			pygame.image.load('src/zombi9.png'),

			pygame.image.load('src/zombi10.png'),
			pygame.image.load('src/zombi10.png'),
			pygame.image.load('src/zombi10.png'),

			pygame.image.load('src/zombi11.png'),
			pygame.image.load('src/zombi11.png'),
			pygame.image.load('src/zombi11.png'),

			pygame.image.load('src/zombi12.png'),
			pygame.image.load('src/zombi12.png'),
			pygame.image.load('src/zombi12.png')
		]
		self.image_anim_count = 0

		self.image = self.move_right[self.image_anim_count]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Zombie Varaible
		self.health = 100
		self.attak = 0.05
		self.speed = 0.75
		self.direction_slop = random.choice([-1,0,1]) # Направление куда будет постоянно уклоняться зомби

	def update(self, pochito_pos, pochito_check_attak):
		
		if self.image_anim_count < len(self.move_right) - 1:
			self.image_anim_count += 1
		else:
			self.image_anim_count = 0
		
		self.image = self.move_right[self.image_anim_count]

		# Moved
		if self.rect.bottom < self.screen_rect.bottom:
			if self.rect.top > self.screen_rect.top + 200:
				if pochito_check_attak: 
					# Если Почито сейчас атакует то нужно всех зомби убрать с его пути

					# Проверяем, может ли нас атаковать Почито
					# Уходим только из под удара

					self.y += self.direction_slop * self.speed
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

