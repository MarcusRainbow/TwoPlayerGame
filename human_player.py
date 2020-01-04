from player import Player
from board import Board

class HumanPlayer(Player):

    def next_move(self, board: Board) -> int: 
        """
        Ask the user, via the console, which move to make
        """
        print(board)
        available = board.available_moves()
        if not available:
            raise Exception("No moves left for you, sorry")

        next = int(input("Your move: "))
        while next not in available:
            next = int(input(f"Please select from {available}: "))
        return next

