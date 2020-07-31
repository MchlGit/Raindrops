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
			self._update_drops()
			self._update_screen()

	def _check_events(self): 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				sys.exit()

	def _get_raincloud_buffer(self): 
		return self.settings.screen_width - self.raincloud.rect.width

	def _get_raindrop_size(self): 
		raindrop = Raindrop(self)
		return raindrop.rect.size

	def _get_drops_per_row(self): 
		raindrop_width, raindrop_height = self._get_raindrop_size()
		available_width = self.settings.screen_width - (self._get_raincloud_buffer() + 2 * raindrop_width)
		return available_width // (2 * raindrop_width)

	def _get_num_rows(self): 
		raindrop_width, raindrop_height = self._get_raindrop_size()
		available_height = self.settings.screen_height - (2*raindrop_height)
		return available_height // (2 * raindrop_height)

	def _get_drop_start_y(self): 
		return int(self.raincloud.rect.height / 2)

	def _update_drops(self): 
		self.drops.update()
		raindrop_width, raindrop_height = self._get_raindrop_size()
		count = 0
		num_drops = self._get_drops_per_row()

		for drop in self.drops.copy(): 
			if drop.rect.bottom > self.settings.screen_height: 
				self.drops.remove(drop)
			elif drop.rect.bottom == self._get_drop_start_y() + 3 * raindrop_height:
				count = count + 1
				print(count)
			if count == num_drops:
				count = 0
				for drop_number in range(num_drops): 
					self._create_drop(drop_number)

	def _create_rain(self): 
		num_drops = self._get_drops_per_row()
		for drop_number in range(num_drops): 
			self._create_drop(drop_number)

	def _create_drop(self, drop_number): 
		new_drop = Raindrop(self)
		drop_width, drop_height = new_drop.rect.size
		new_drop.x = drop_number * drop_width * 2 + self._get_raincloud_buffer()//2 + 2*drop_width

		new_drop.rect.x = int(new_drop.x)
		new_drop.rect.y = self._get_drop_start_y()

		self.drops.add(new_drop)

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.drops.draw(self.screen)
		self.raincloud.blitme()
		pygame.display.flip()

if __name__ == "__main__":
	raindrops = Raindrops()
	raindrops.run_game() 
