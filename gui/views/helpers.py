import pygame

from gui.settings.display import DISPLAY_SCALING


def get_text_objects(text, font):
	text_surface = font.render(text, True, pygame.Color("black"))
	return text_surface, text_surface.get_rect()


def message_display(surface, text, pos=None, font='freesansbold.ttf', size=60, center=True):
	if pos is None:
		pos_x, pos_y = surface.get_width() / 2, surface.get_height() / 2
	else:
		pos_x, pos_y = pos

	large_text = pygame.font.SysFont(font, size * DISPLAY_SCALING)
	text_surf, text_rect = get_text_objects(text, large_text)
	
	if center:
		text_rect.center = (pos_x, pos_y)
	else:
		text_rect.topleft = (pos_x, pos_y)
	
	surface.blit(text_surf, text_rect)


def draw_color_box(surface, border_color, border_thickness, inner_color, coords, size):
    """Coords: (x, y); Size (w, h)"""
    x, y = coords  # todo pass these as named tuples
    w, h = size
    
    pygame.draw.rect(surface, border_color, (x, y, w, h))
    pygame.draw.rect(surface, inner_color,
                     (x+border_thickness, y+border_thickness, w-2*border_thickness, h-2*border_thickness))
