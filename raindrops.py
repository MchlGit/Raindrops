import pygame 
import sys 
from settings import Settings 
from raincloud import Raincloud
from raindrop import Raindrop

class Raindrops: 

	def __init__(self): 
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		self.raincloud = Raincloud(self)
		pygame.display.set_caption("Raindrops Keep Falling On My Head")

		self.drops = pygame.sprite.Group()
		self._create_rain()

	def run_game(self): 
		while True: 
			self._check_events()
			self._update_screen()

	def _check_events(self): 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				sys.exit()

	def _create_rain(self): 
		raindrop = Raindrop(self)
		raindrop_width, raindrop_height = raindrop.rect.size
		raincloud_height = self.raincloud.rect.height
		raincloud_buffer = self.settings.screen_width - self.raincloud.rect.width

		available_width = self.settings.screen_width - (raincloud_buffer + 2 * raindrop_width)
		num_drops = available_width // (2 * raindrop_width)
		print(num_drops)
		print(available_width)
		print(raindrop_width)

		available_height = self.settings.screen_height - (2*raindrop_height)
		num_rows = available_height // (2 * raindrop_height)
		print(num_rows)
		print(available_height)
		print(raindrop_height)
		print(raincloud_height)#600 screen height

		for row_number in range(num_rows): 
			for drop_number in range(num_drops): 
				self._create_drop(drop_number, row_number)

	def _create_drop(self, drop_number, row_number): 
		raincloud_buffer = self.settings.screen_width - self.raincloud.rect.width

		raincloud_height = self.raincloud.rect.height
		new_drop = Raindrop(self)
		drop_width, drop_height = new_drop.rect.size
		new_drop.x = drop_number * drop_width * 2 + raincloud_buffer//2 + 2*drop_width

		new_drop.rect.x = int(new_drop.x)
		new_drop.rect.y = row_number * drop_height * 2 + raincloud_height//2 + drop_height

		self.drops.add(new_drop)

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.raincloud.blitme()
		self.drops.draw(self.screen)
		pygame.display.flip()

if __name__ == "__main__":
	raindrops = Raindrops()
	raindrops.run_game() 
