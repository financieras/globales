# config.py

from enum import Enum

class PieceColor(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

class TerminalColor(Enum):
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    WHITE = "\033[0;37m"
    RESET = "\033[0m"
    GRAY = "\033[2;30m"
    BOLD = "\033[1m"

class Direction(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)
    NORTHEAST = (-1, 1)
    NORTHWEST = (-1, -1)
    SOUTHEAST = (1, 1)
    SOUTHWEST = (1, -1)

class GameConstants:
    def __init__(self):
        self.BOARD_SIZE = 920
        self.COLS = 19
        self.ROWS = 19
        self.GRID_SIZE = self.COLS - 1
        self.MARGIN = 90
        self.BORDER_MARGIN = 30
        self.CELL_SIZE = (self.BOARD_SIZE - 2 * self.MARGIN) // self.GRID_SIZE
        self.BORDER_COLOR = (150, 150, 150)
        self.WOOD = (222, 184, 135)
        self.RED = (150, 0, 0)
        self.total_score = {PieceColor.BLACK: 0, PieceColor.WHITE: 0}
        self.current_player = PieceColor.BLACK

g = GameConstants()
