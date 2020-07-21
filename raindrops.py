import pygame 
import sys 
from settings import Settings 

class Raindrops: 

	def __init__(self): 
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Raindrops Keep Falling On My Head")

	def run_game(self): 
		while True: 
			self._check_events()
			self._update_screen()

	def _check_events(self): 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				sys.exit()


	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		pygame.display.flip()

if __name__ == "__main__":
	raindrops = Raindrops()
	raindrops.run_game() 
