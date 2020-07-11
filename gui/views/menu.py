import pygame

from gui.settings.display import DISPLAY_SCALING
from gui.settings.color_scheme import PURPLE, PURPLE_HIGHLIGHT
from gui.views.menu_background import Background
from gui.views.helpers import message_display, Button


class Menu:
	# todo decide how to nicely handle these values
	
	# Menu buttons
	BUTTON_LABELS = ["Single Player", "Two Player", "Demo", "Quit"]
	
	# menu button properties
	_BUTTON_WIDTH = 300 * DISPLAY_SCALING
	_BUTTON_HEIGHT = 50 * DISPLAY_SCALING
	_BUTTON_Y_SPACING = 1.5
	_BUTTON_X_SPACING = 0.5

	def __init__(self, screen: pygame.Surface):
		self.screen = screen
		self.background = Background(screen)

		self.screen_width = self.screen.get_width()
		self.screen_height = self.screen.get_height()

		# Compute locations of buttons & add predefined common colors
		self.COMMON_BUTTON_PROPERTIES = {
			"x": (self.screen_width - self._BUTTON_WIDTH) / 2,
			'w': self._BUTTON_WIDTH, 'h': self._BUTTON_HEIGHT, 'ic': PURPLE, 'ac': PURPLE_HIGHLIGHT, 
		}

		self.MENU_BUTTON_PROPERTIES = [  # todo add names instead of integers as keys
			{"y": (self.screen_height/3) + (i + 1) * self._BUTTON_HEIGHT * self._BUTTON_Y_SPACING } 
			for i in range(len(self.BUTTON_LABELS))
		]

		self.buttons = []

		# create button object with common & calculated button properties
		for idx, button_properties in enumerate(self.MENU_BUTTON_PROPERTIES):
			button_properties.update(self.COMMON_BUTTON_PROPERTIES)

			self.buttons.append(
				Button(msg=self.BUTTON_LABELS[idx], **self.MENU_BUTTON_PROPERTIES[idx])
			)


	def render(self):
		self.screen.fill(pygame.Color("white"))

		self.background.update()

		message_display(surface=self.screen, text="Ultimate Tic Tac Toe", pos=(self.screen.get_width() / 2, self.screen.get_height() / 3),
						font='comicsansms', size=40)

		# only ask for mouse & click status once and not for every button
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		for button in self.buttons:
			button.render(self.screen, mouse, click)
