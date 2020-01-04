from player import Player
from board import Board
from random import choice

class RandomPlayer(Player):

    """
    A player that simply randomly selects a move
    """
    def next_move(self, board: Board) -> int:
        possible_moves = board.available_moves()
        if not possible_moves:
            raise Exception("I cannot move")
        return choice(possible_moves)
