import abc
from board import Board

class Player(abc.ABC):
    """
    Defines a player in the game. The player may be human, machine,
    real or virtual.
    """
    @abc.abstractmethod
    def next_move(self, board: Board) -> int:
        pass
