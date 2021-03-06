from itertools import count
from enum import IntEnum, Enum, auto

from gui.settings.display import DISPLAY_SCALING, DISPLAY_WIDTH, DISPLAY_HEIGHT
from gui.settings.color_scheme import *


BOARD_WIDTH = DISPLAY_WIDTH * 4//5 * DISPLAY_SCALING
BOARD_HEIGHT = DISPLAY_HEIGHT * 4//5 * DISPLAY_SCALING


Grid = IntEnum('Grid', zip([
    'TOP_LEFT', 'TOP_MIDDLE', 'TOP_RIGHT',
    'MIDDLE_LEFT', 'MIDDLE_MIDDLE', 'MIDDLE_RIGHT',
    'BOTTOM_LEFT', 'BOTTOM_MIDDLE', 'BOTTOM_RIGHT'], count()))


BORDER_THICKNESS = 2
BORDERS = {
    Grid.TOP_LEFT:      (0, 0, -BORDER_THICKNESS, -BORDER_THICKNESS),
    Grid.TOP_MIDDLE:    (BORDER_THICKNESS, 0, -2 * BORDER_THICKNESS, -BORDER_THICKNESS),
    Grid.TOP_RIGHT:     (BORDER_THICKNESS, 0, -BORDER_THICKNESS, -BORDER_THICKNESS),

    Grid.MIDDLE_LEFT:   (0, BORDER_THICKNESS, -BORDER_THICKNESS, -2 * BORDER_THICKNESS),
    Grid.MIDDLE_MIDDLE: (BORDER_THICKNESS, BORDER_THICKNESS, -2 * BORDER_THICKNESS, -2 * BORDER_THICKNESS),
    Grid.MIDDLE_RIGHT:  (BORDER_THICKNESS, BORDER_THICKNESS, -BORDER_THICKNESS, -2 * BORDER_THICKNESS),

    Grid.BOTTOM_LEFT:   (0, BORDER_THICKNESS, -BORDER_THICKNESS, -BORDER_THICKNESS),
    Grid.BOTTOM_MIDDLE: (BORDER_THICKNESS, BORDER_THICKNESS, -2 * BORDER_THICKNESS, -BORDER_THICKNESS),
    Grid.BOTTOM_RIGHT:  (BORDER_THICKNESS, BORDER_THICKNESS, -BORDER_THICKNESS, -BORDER_THICKNESS),
}

SUB_GRID_PADDING = 11
MAIN_BOX_WIDTH = BOARD_WIDTH / 3
MAIN_BOX_HEIGHT = BOARD_HEIGHT / 3
CELL_WIDTH = MAIN_BOX_WIDTH / 3
CELL_HEIGHT = MAIN_BOX_HEIGHT / 3
# offset for main grid from main window
OFFSET_X, OFFSET_Y = (DISPLAY_WIDTH - BOARD_WIDTH) / 2, (DISPLAY_HEIGHT - BOARD_HEIGHT) / 2


# GRID_RESULT_COLORS = {
#     PLAYER_X: RED_HIGHLIGHT,
#     PLAYER_O: BLUE_HIGHLIGHT,
#     DRAW: GREY
# }

BORDER_COLOR = BLACK
BOX_COLOR = WHITE

# In these parameters the values for x & y will the added to the current position computed for each grid cell
MAIN_GRID_DRAW_PARAMETERS = [
    {'border': Grid.TOP_LEFT, 'border_colour': BORDER_COLOR, 'box_colour': BOX_COLOR,
     'x': OFFSET_X, 'y': OFFSET_Y,
     'w': MAIN_BOX_WIDTH, 'h': MAIN_BOX_HEIGHT},
    {'border': Grid.TOP_MIDDLE, 'border_colour': BORDER_COLOR, 'box_colour': BOX_COLOR,
     'x': OFFSET_X + BOARD_WIDTH / 3, 'y': OFFSET_Y,
     'w': MAIN_BOX_WIDTH, 'h': MAIN_BOX_HEIGHT},
    {'border': Grid.TOP_RIGHT, 'border_colour': BORDER_COLOR, 'box_colour': BOX_COLOR,
     'x': OFFSET_X + BOARD_WIDTH * (2 / 3), 'y': OFFSET_Y,
     'w': MAIN_BOX_WIDTH, 'h': MAIN_BOX_HEIGHT},
    # middle row
    {'border': Grid.MIDDLE_LEFT, 'border_colour': BORDER_COLOR, 'box_colour': BOX_COLOR,
     'x': OFFSET_X, 'y': OFFSET_Y + BOARD_HEIGHT / 3,
     'w': MAIN_BOX_WIDTH, 'h': MAIN_BOX_HEIGHT},
    {'border': Grid.MIDDLE_MIDDLE, 'border_colour': BORDER_COLOR, 'box_colour': BOX_COLOR,
     'x': OFFSET_X + BOARD_WIDTH / 3, 'y': OFFSET_Y + BOARD_HEIGHT / 3,
     'w': MAIN_BOX_WIDTH, 'h': MAIN_BOX_HEIGHT},
    {'border': Grid.MIDDLE_RIGHT, 'border_colour': BORDER_COLOR, 'box_colour': BOX_COLOR,
     'x': OFFSET_X + BOARD_WIDTH * (2 / 3), 'y': OFFSET_Y + BOARD_HEIGHT / 3,
     'w': MAIN_BOX_WIDTH, 'h': MAIN_BOX_HEIGHT},
    # bottom row
    {'border': Grid.BOTTOM_LEFT, 'border_colour': BORDER_COLOR, 'box_colour': BOX_COLOR,
     'x': OFFSET_X, 'y': OFFSET_Y + BOARD_HEIGHT * (2 / 3),
     'w': MAIN_BOX_WIDTH, 'h': MAIN_BOX_HEIGHT},
    {'border': Grid.BOTTOM_MIDDLE, 'border_colour': BORDER_COLOR, 'box_colour': BOX_COLOR,
     'x': OFFSET_X + BOARD_WIDTH / 3, 'y': OFFSET_Y + BOARD_HEIGHT * (2 / 3),
     'w': MAIN_BOX_WIDTH, 'h': MAIN_BOX_HEIGHT},
    {'border': Grid.BOTTOM_RIGHT, 'border_colour': BORDER_COLOR, 'box_colour': BOX_COLOR,
     'x': OFFSET_X + BOARD_WIDTH * (2 / 3), 'y': OFFSET_Y + BOARD_HEIGHT * (2 / 3),
     'w': MAIN_BOX_WIDTH, 'h': MAIN_BOX_HEIGHT},
]


