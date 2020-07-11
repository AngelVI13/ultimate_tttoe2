import pygame

from gui.settings.display import DISPLAY_SCALING


def get_text_objects(text, font):
	text_surface = font.render(text, True, pygame.Color("black"))
	return text_surface, text_surface.get_rect()

def message_display(surface, text, pos=None, font='freesansbold.ttf', size=60):
	if pos is None:
		pos_x, pos_y = surface.get_width() / 2, surface.get_height() / 2
	else:
		pos_x, pos_y = pos

	large_text = pygame.font.SysFont(font, size * DISPLAY_SCALING)
	text_surf, text_rect = get_text_objects(text, large_text)
	text_rect.center = (pos_x, pos_y)
	surface.blit(text_surf, text_rect)


class Button:
	text_font = None

	def __init__(self, x, y, w, h, msg, ic, ac, action=None):
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

	def render(self, surface, mouse, click):
		if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
			pygame.draw.rect(surface, self.ac, self.box)
			
			if click[0] == 1 and self.action is not None:
				self.action()
		else:
			pygame.draw.rect(surface, self.ic, self.box)

		surface.blit(self.text_surf, self.text_rect)
