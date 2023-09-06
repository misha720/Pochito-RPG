import pygame

class Pochito(pygame.sprite.Sprite):
	'''Класс Pochito'''
	def __init__(self, screen, x, y):
		super(Pochito,self).__init__()
		self.screen = screen
		self.screen_rect = self.screen.get_rect() # Получаем границы экрана
		self.image = pygame.image.load('src/pochito_bottom1.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = 5
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
	
	def drawing(self):
		self.screen.blit( self.image, ( self.x, self.y, ) )
	
	def update(self, move: list):
		
		if self.rect.bottom < self.screen_rect.bottom:
			if self.rect.top > self.screen_rect.top:
				if self.rect.right < self.screen_rect.right:
					if self.rect.left > self.screen_rect.left:
						self.x += move[0] * self.speed
						self.y += move[1] * self.speed
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
		