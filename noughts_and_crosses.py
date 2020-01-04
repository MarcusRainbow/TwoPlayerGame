from game import Game
from board import Board
import numpy as np
from typing import Tuple
from human_player import HumanPlayer
from clever_player import CleverPlayer
from play import play_game

class NoughtsAndCrosses(Game):
    def clean_board(self) -> Board:
        return Board(np.zeros((3, 3), dtype=int), lambda grid:
            [i for i, j in enumerate(np.nditer(grid)) if j == 0])

    def tokens(self) -> Tuple[int, int]:
        return (-1, 1)

    def test_win(self, board: Board) -> int:
        """
        A win in noughts and crosses is a line of three the
        same in any row column or diagonal
        """
        row_sums = board.grid.sum(axis=0)
        if 3 in row_sums:
            return 1
        if -3 in row_sums:
            return 0
        col_sums = board.grid.sum(axis=1)
        if 3 in col_sums:
            return 1
        if -3 in col_sums:
            return 0
        diag_sum = board.grid.trace()
        if 3 == diag_sum:
            return 1
        if -3 == diag_sum:
            return 0
        sinister_sum = np.fliplr(board.grid).trace()
        if 3 == sinister_sum:
            return 1
        if -3 == sinister_sum:
            return 0

        # nobody won
        return -1

if __name__ == "__main__":
    game = NoughtsAndCrosses()
    play_game(HumanPlayer(), CleverPlayer(game, 1, 100), game)