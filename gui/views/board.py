import pygame
from itertools import count
from enum import IntEnum, Enum, auto
from functools import total_ordering

from gui.views.helpers import message_display
from gui.settings.color_scheme import RED, BLUE, RED_HIGHLIGHT, BLUE_HIGHLIGHT, BLACK, WHITE
from gui.settings.display import DISPLAY_SCALING, DISPLAY_WIDTH, DISPLAY_HEIGHT
from board.constants import PLAYER_X, PLAYER_O


BOARD_WIDTH = 480 * DISPLAY_SCALING
BOARD_HEIGHT = 480 * DISPLAY_SCALING


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


@total_ordering
class Cell:
    """Defines a hashable cell container. Used to store info for all cells in all subgrids."""

    __slots__ = ['pos_x', 'pos_y', 'width', 'height', 'player', 'board_idx', 'cell_idx']

    def __init__(self, pos_x, pos_y, width, height, player, board_idx=None, cell_idx=None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.player = player
        self.board_idx = board_idx
        self.cell_idx = cell_idx

    def __repr__(self):  # todo only used for debugging
        return '{}(board={}, cell={})'.format(self.__class__.__name__, self.board_idx, self.cell_idx)

    def __hash__(self):
        return hash((self.pos_x, self.pos_y))

    def __eq__(self, other):
        return self.pos_x == other.pos_x and self.pos_y == other.pos_y

    def __lt__(self, other):
        return self.pos_x < other.pos_x and self.pos_y < other.pos_y


class Board:
    colors = {
        PLAYER_X: RED,
        PLAYER_O: BLUE,
    }
    
    clicked_cells = set()  # a set of all clicked cells
    all_cells = set()  # a set of all created cells
    all_grids = set()  # a set of all subgrids

    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay

    def draw_subcell(self, border, border_colour, box_colour, x, y, w, h, grid_idx):
        # Draw bounding box of cell
        mod_x, mod_y, mod_w, mod_h = BORDERS[border]
        pygame.draw.rect(self.gameDisplay, border_colour, (x, y, w, h))

        inner_x, inner_y, inner_w, inner_h = x + mod_x, y + mod_y, w + mod_w, h + mod_h

        # keep track of all cells on the board
        cell = Cell(pos_x=inner_x, pos_y=inner_y, width=inner_w, height=inner_h,
                    player=None, board_idx=grid_idx, cell_idx=border)
        if cell not in self.all_cells:
            self.all_cells.add(cell)

        # draw inner box of cell (main content)
        pygame.draw.rect(self.gameDisplay, box_colour, (inner_x, inner_y, inner_w, inner_h))

    def draw_sub_grid(self, border, border_colour, box_colour, x, y, w, h):
        # todo maybe turn this into a method to clean up the logic
        # draw bounding box of subgrid
        mod_x, mod_y, mod_w, mod_h = BORDERS[border]
        pygame.draw.rect(self.gameDisplay, border_colour, (x, y, w, h))
        # update position and size values for inner rectangle
        x, y = x + mod_x, y + mod_y
        w, h = w + mod_w, h + mod_h
        pygame.draw.rect(self.gameDisplay, box_colour, (x, y, w, h))

        # keep track of all subgrids. NOTE: here 'border' is the index of the subgrid on the main grid.
        grid = Cell(pos_x=x, pos_y=y, width=w, height=h, player=None, board_idx=border, cell_idx=None)
        if grid not in self.all_grids:
            self.all_grids.add(grid)

        # calculate inner box for subgrid
        cell_size = min(w, h)
        x, y = x + 2 * SUB_GRID_PADDING, y + 2 * SUB_GRID_PADDING
        w = h = cell_size - 4 * SUB_GRID_PADDING
        cell_width_ = w / 3
        cell_height_ = h / 3

        positions = [
            # top row
            {'border': Grid.TOP_LEFT,      'x': x, 'y': y},
            {'border': Grid.TOP_MIDDLE,    'x': x + w * (1 / 3), 'y': y},
            {'border': Grid.TOP_RIGHT,     'x': x + w * (2 / 3), 'y': y},

            # middle row
            {'border': Grid.MIDDLE_LEFT,   'x': x, 'y': y + (h / 3)},
            {'border': Grid.MIDDLE_MIDDLE, 'x': x + w * (1 / 3), 'y': y + (h / 3)},
            {'border': Grid.MIDDLE_RIGHT,  'x': x + w * (2 / 3), 'y': y + (h / 3)},

            # bottom row
            {'border': Grid.BOTTOM_LEFT,   'x': x, 'y': y + h * (2 / 3)},
            {'border': Grid.BOTTOM_MIDDLE, 'x': x + w * (1 / 3), 'y': y + h * (2 / 3)},
            {'border': Grid.BOTTOM_RIGHT,  'x': x + w * (2 / 3), 'y': y + h * (2 / 3)},
        ]

        for position in positions:
            # here border is the index of which grid all of the cells are part of
            self.draw_subcell(**position, border_colour=border_colour, box_colour=box_colour, w=cell_width_,
                              h=cell_height_, grid_idx=border)

    def draw_main_grid(self):
        for parameters in MAIN_GRID_DRAW_PARAMETERS:
            self.draw_sub_grid(**parameters)

    def draw_clicked_cells(self):
        for cell in self.clicked_cells:
            pygame.draw.rect(self.gameDisplay, self.colors[cell.player],
                             (cell.pos_x, cell.pos_y, cell.width, cell.height))

    def draw_side_to_move(self, player_to_move):
        """Draws side to move in top left corner of screen (game screen)"""
        # todo remove magic numbers
        pygame.draw.rect(self.gameDisplay, BLACK, (OFFSET_X+8, OFFSET_Y-22, 24, 14))
        pygame.draw.rect(self.gameDisplay, self.colors[player_to_move], (OFFSET_X+10, OFFSET_Y-20, 20, 10))
        message_display(surface=self.gameDisplay, text=' to move', pos=(OFFSET_X+55, OFFSET_Y-15), font='comicsansms', size=16)

    def draw_color_box(self, border_color, border_thickness, inner_color, coords, size):
        """Coords: (x, y); Size (w, h)"""
        x, y = coords  # todo pass these as named tuples
        w, h = size
        # (OFFSET_X + 8, OFFSET_Y - 22, 24, 14)
        pygame.draw.rect(self.gameDisplay, border_color, (x, y, w, h))
        pygame.draw.rect(self.gameDisplay, inner_color,
                         (x+border_thickness, y+border_thickness, w-2*border_thickness, h-2*border_thickness))

    def render(self):
        self.gameDisplay.fill(WHITE)
        self.draw_main_grid()

        # if not self.allowed_cells:
        #     self.allowed_cells = self.find_allowed_cells()

        # Need to wait a bit before allowing user input otherwise the menu click gets detected
        # as game click
        # if time.time() - start > PAUSE_BEFORE_USER_INPUT:
        #     self.get_game_input(game_type, pos)

        self.draw_clicked_cells()
        # self.draw_results()
        # self.draw_allowed_moves(highlight)
        self.draw_side_to_move(PLAYER_X) # replace with below
        # self.draw_side_to_move(-self.board.playerJustMoved)
