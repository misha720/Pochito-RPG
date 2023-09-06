import pygame

class Zombie(pygame.sprite.Sprite):
	'''Класс Zombie'''
	def __init__(self, screen, x, y):
		super(Zombie,self).__init__()
		self.screen = screen
		self.screen_rect = self.screen.get_rect() # Получаем границы экрана

		self.move_right = [
			pygame.image.load('src/zombi1.png'),
			pygame.image.load('src/zombi2.png'),
			pygame.image.load('src/zombi3.png'),
			pygame.image.load('src/zombi4.png'),
			pygame.image.load('src/zombi5.png'),
			pygame.image.load('src/zombi6.png'),
			pygame.image.load('src/zombi7.png'),
			pygame.image.load('src/zombi8.png'),
			pygame.image.load('src/zombi9.png'),
			pygame.image.load('src/zombi10.png'),
			pygame.image.load('src/zombi11.png'),
			pygame.image.load('src/zombi12.png')
		]
		self.image_anim_count = 0

		self.image = self.move_right[0]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		self.speed = 0.75
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def drawing(self):
		self.screen.blit( self.move_right[self.image_anim_count], ( self.x, self.y, ) )

	def update(self):
		if self.image_anim_count < len(self.move_right) - 1:
			self.image_anim_count += 1
		else:
			self.image_anim_count = 0

		self.x -= 1 * self.speed
		self.y += 0

		self.rect.x = self.x 
		self.rect.y = self.y
		
		