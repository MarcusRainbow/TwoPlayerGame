from typing import List
import numpy as np

class Board:
    """
    Represents the state of the game, and says which moves
    are available.
    """
    def __init__(self, grid: np.ndarray, available):
        self.grid = np.copy(grid)
        self.available = available

    def clone(self):
        return Board(self.grid, self.available)

    def available_moves(self) -> List[int]:
        return self.available(self.grid)

    def apply_move(self, pos: int, token: int):
        """
        Apply a players move.
        """
        self.grid.flat[pos] = token
        
    def __str__(self) -> str:
        return f"{self.grid}"