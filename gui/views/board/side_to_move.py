import pygame

from gui.views.board.defines import *
from gui.views.helpers import message_display, draw_color_box
from gui.settings.color_scheme import PLAYER_COLORS


class SideToMove:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.box = pygame.Rect(
            OFFSET_X, OFFSET_Y // 2,  # x, y 
            24 * DISPLAY_SCALING, 14 * DISPLAY_SCALING  # w, h
        )

    def render(self, player_to_move):
        """Draws side to move in top left corner of screen (game screen)"""
        
        draw_color_box(
            surface=self.screen,
            border_color=BLACK, 
            border_thickness=BORDER_THICKNESS, 
            inner_color=PLAYER_COLORS[player_to_move], 
            coords=self.box.topleft, 
            size=self.box.size
        )

        message_display(
            surface=self.screen, 
            text=' to move', 
            pos=(self.box.x + self.box.w, self.box.y - BORDER_THICKNESS), 
            font='comicsansms', 
            size=16 * DISPLAY_SCALING,
            center=False
        )
