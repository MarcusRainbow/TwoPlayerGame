from game import Game
from board import Board
import numpy as np
from typing import Tuple, List

class Connect4(Game):
    def __init__(self, starting_grid = np.zeros((6, 7), dtype=int)):
        self.starting_grid = starting_grid

    def clean_board(self) -> Board:
        return Board(np.copy(self.starting_grid), lambda grid: legal_moves(grid))   

    def tokens(self) -> Tuple[int, int]:
        return (-1, 1)

    def test_win(self, board: Board) -> int:
        """
        A win in connect 4 is a line of 4 the same in any
        row column or diagonal
        """
        if are_four_connected(-1, board.grid):
            return 0
        elif are_four_connected(1, board.grid):
            return 1
        else:
            return -1

def legal_moves(grid: np.ndarray) -> List[int]:
    """
    You can legally place a token at the bottom of any column,
    above any other previous tokens
    """
    cols = np.size(grid, 1)
    result = []

    for x, column in enumerate(np.transpose(grid)):
        # find the first zero element
        y = np.where(column == 0)
        if len(y[0]) > 0:
            pos = x + y[0][0] * cols
            result.append(pos)

    return result

def are_four_connected(player: int, grid: np.ndarray) -> bool:
    """
    Algorithm from stack overflow. Converted from Java.
    """
    cols = np.size(grid, 1)
    rows = np.size(grid, 0)

    # horizontalCheck 
    for x in range(cols - 3):
        for y in range(rows):
            if (grid[y, x] == player and grid[y, x+1] == player
                and grid[y, x+2] == player and grid[y, x+3] == player):
                return True

    # verticalCheck
    for y in range(rows - 3):
        for x in range(cols):
            if (grid[y, x] == player and grid[y+1, x] == player
                and grid[y+2, x] == player and grid[y+3, x] == player):
                return True
            
    # ascendingDiagonalCheck 
    for y in range(3, rows):
        for x in range(cols - 3):
            if (grid[y, x] == player and grid[y-1, x+1] == player
                and grid[y-2, x+2] == player and grid[y-3, x+3] == player):
                return True

    # descendingDiagonalCheck
    for y in range(3, rows):
        for x in range(3, cols):
            if (grid[y, x] == player and grid[y-1, x-1] == player
                and grid[y-2, x-2] == player and grid[y-3, x-3] == player):
                return True

    return False

if __name__ == "__main__":
    from play import play_game
    from human_player import HumanPlayer
    from clever_player import CleverPlayer

    game = Connect4()
    play_game(HumanPlayer(), CleverPlayer(game, 1, 4), game)
