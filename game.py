import abc
from board import Board
from typing import Tuple

class Game(abc.ABC):
    """
    Defines a game, such as Go or nought and crosses.
    """

    @abc.abstractmethod
    def clean_board(self) -> Board:
        """
        Factory method that produces a clean board.
        """
        pass

    @abc.abstractmethod
    def tokens(self) -> Tuple[int, int]:
        """
        Returns a tuple of the token for player 0
        followed by the token for player 1
        """
        pass

    @abc.abstractmethod
    def test_win(self, board: Board) -> int:
        """
        If there is no winner, returns -1. If player0 is
        the winner, returns 0. If player1 is the winner,
        returns 1.
        """
        pass
