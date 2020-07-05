import pygame

from gui.settings import DISPLAY_SCALING
from gui.views.menu_background import Background
from gui.views.helpers import message_display, button


class Menu:
	def __init__(self, screen: pygame.Surface):
		self.screen = screen
		self.background = Background(screen)

		self.font_instance = pygame.font.Font(None, 30)  # todo what are these params

		self.screen_width = self.screen.get_width()
		self.screen_height = self.screen.get_height()

		# todo decide how to nicely handle these values
		self._BUTTON_WIDTH = 300 * DISPLAY_SCALING
		self._BUTTON_HEIGHT = 50 * DISPLAY_SCALING
		self._BUTTON_Y_SPACING = 1.5
		self._BUTTON_X_SPACING = 0.5

		PURPLE = (0x6c, 0x6e, 0xA0)
		PURPLE_HIGHLIGHT = (0x59, 0x5b, 0x83)

		self.COMMON_BUTTON_PROPERTIES = {
			"x": (self.screen_width - self._BUTTON_WIDTH) / 2,
			'w': self._BUTTON_WIDTH, 'h': self._BUTTON_HEIGHT, 'ic': PURPLE, 'ac': PURPLE_HIGHLIGHT, 
		}

		self.MENU_BUTTON_PROPERTIES = [  # todo add names instead of integers as keys
			{"y": (self.screen_height/3) + (i + 1) * self._BUTTON_HEIGHT * self._BUTTON_Y_SPACING } 
			for i in range(4)
		]
		for button_properties in self.MENU_BUTTON_PROPERTIES:
			button_properties.update(self.COMMON_BUTTON_PROPERTIES)


	def render(self):
		self.screen.fill(pygame.Color("white"))
		# text_surface = self.font_instance.render(
		# 	"Menu. (space to play, esc to exit)", True, pygame.Color("black")
		# )
		# text_rect = text_surface.get_rect()
		# text_rect.center = ()
		# self.screen.blit(text, (0, 0))
		self.background.update()

		message_display(surface=self.screen, text="Ultimate Tic Tac Toe", pos=(self.screen.get_width() / 2, self.screen.get_height() / 3),
						font='comicsansms', size=40)

		button(self.screen, msg="Single Player", **self.MENU_BUTTON_PROPERTIES[0])
				# action=partial(self.game_loop, GameType.SINGLE_PLAYER))
		button(self.screen, msg="Two Player", **self.MENU_BUTTON_PROPERTIES[1],)
		# 			action=partial(self.game_loop, GameType.MULTI_PLAYER))
		button(self.screen, msg="Demo", **self.MENU_BUTTON_PROPERTIES[2],)
				# action=partial(self.game_loop, GameType.DEMO_MODE))
		button(self.screen, msg="Quit", **self.MENU_BUTTON_PROPERTIES[3],) 
				# action=self.quit_game)

