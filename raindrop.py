import pygame 
from pygame.sprite import Sprite 

class Raindrop(Sprite): 

	def __init__(self, raindrops_game): 
		super().__init__()
		self.screen = raindrops_game.screen
		self.settings = raindrops_game.settings

		self.image = pygame.image.load("images/raindrop.bmp")
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#self.y = float(self.rect.y)

	def update(self): 
		self.rect.y += self.settings.drop_speed
		#self.rect.y = self.y