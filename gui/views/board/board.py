import pygame

from gui.views.board.cell import Cell
from gui.views.board.defines import *
from gui.views.board.side_to_move import SideToMove
from gui.settings.color_scheme import *
from gui.settings.display import DISPLAY_SCALING
from board.constants import PLAYER_X, PLAYER_O


class Board:
    clicked_cells = set()  # a set of all clicked cells
    all_cells = set()  # a set of all created cells
    all_grids = set()  # a set of all subgrids

    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay

        self.side_to_move_view = SideToMove(self.gameDisplay)

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
        self.side_to_move_view.render(PLAYER_X) # replace with below
        # self.side_to_move_view.render(-self.board.playerJustMoved)
