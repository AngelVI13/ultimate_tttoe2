import pygame

from gui.views.helpers import get_text_objects 
from gui.settings.display import DISPLAY_SCALING


class Button:
	text_font = None

	def __init__(self, x, y, w, h, msg, ic, ac, action):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.msg = msg
		self.ic = ic # inactive color
		self.ac = ac # active color
		self.action = action # action type i.e. Play, Quit etc.

		# initialize font if not done already
		if self.text_font is None:
			self.text_font = pygame.font.SysFont("comicsansms", 20 * DISPLAY_SCALING)

		# Text object (Rect + Surf)
		self.text_surf, self.text_rect = get_text_objects(self.msg, self.text_font)
		self.text_rect.center = self.x + (self.w / 2), self.y + (self.h / 2)

		self.box = pygame.Rect(self.x, self.y, self.w, self.h)

	def render(self, surface, mouse):
		if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
			pygame.draw.rect(surface, self.ac, self.box)
		else:
			pygame.draw.rect(surface, self.ic, self.box)

		surface.blit(self.text_surf, self.text_rect)
