import pygame

from gui.settings import DISPLAY_SCALING


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

def button(surface, msg, x, y, w, h, ic, ac, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	# print(click)
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(surface, ac, (x, y, w, h))

		if click[0] == 1 and action is not None:
			action()
	else:
		pygame.draw.rect(surface, ic, (x, y, w, h))

	small_text = pygame.font.SysFont("comicsansms", 20 * DISPLAY_SCALING)
	text_surf, text_rect = get_text_objects(msg, small_text)
	text_rect.center = ((x + (w / 2)), (y + (h / 2)))
	surface.blit(text_surf, text_rect)