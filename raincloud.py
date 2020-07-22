import pygame 
from pygame.sprite import Sprite

class Raincloud(Sprite): 

	def __init__(self, raindrops_game): 
		super().__init__()
		self.screen = raindrops_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = raindrops_game.settings

		self.image = pygame.image.load("images/raincloud.bmp")
		self.rect = self.image.get_rect()

		self.rect.midtop = self.screen_rect.midtop

	def blitme(self): 
		self.screen.blit(self.image, self.rect)


