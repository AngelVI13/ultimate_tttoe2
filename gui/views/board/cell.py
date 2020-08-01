from functools import total_ordering


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
