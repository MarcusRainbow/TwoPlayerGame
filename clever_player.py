from player import Player
from board import Board
from game import Game
from random import choice
from typing import Tuple

class CleverPlayer(Player):
    """
    A player that tries to win, assuming it is playing
    against the same sort of player.
    """
    def __init__(self, game: Game, player: int, depth: int, other = None):
        self.game = game
        self.player = player
        self.depth = depth
        tokens = game.tokens()
        self.token = tokens[player]
        other_player = 0 if player == 1 else 1
        # While thinking about a move, we need a
        # clever opponent
        if other:
            self.other = other
        else:
            self.other = CleverPlayer(game, other_player, depth - 1, self)

    def next_move(self, board: Board) -> int:
        """
        Finds the best possible move from this point, trying to
        win, or at least force a draw.
        """
        if not board.available_moves():
            raise Exception("I cannot move")

        return self.best_move(board, self.depth)[0]

    def best_move(self, board: Board, depth: int) -> Tuple[int, int]:
        """
        Finds the best available move for this player, and returns
        a tuple of the best move, followed by the quality of the
        move (-1 = draw, 0 = player 0 win, 1 = player 2 win)
        """
        possible_moves = board.available_moves()
        if not possible_moves:
            return -1, -1

        # if we have descended too far into our thought processes
        # without an answer, treat it as a draw and pick one
        # choice at random
        if depth <= 0:
            # print("too deep. Returning random choice")
            return choice(possible_moves), -1

        draw = -1
        for move in possible_moves:

            # try out this move
            test_board = board.clone()
            test_board.apply_move(move, self.token)
            # print(f"try {move} for player {self.player}")
            winner = self.game.test_win(test_board)
            if winner == self.player:
                # Immediate win. Play this move
                # print(f"Win: {move} for player {self.player}")
                return move, winner
            elif winner == self.other.player:
                # immediate lose. Do not play this move
                # print(f"Lose: {move} for player {self.player}")
                continue
            elif not test_board.available_moves():
                # this move results in a stalemate. Only play if forced
                draw = move
                continue
            else:
                # if we get to here, we have available moves but do not
                # yet know if they result in a win or lose. Ask our
                # opponent to make their best move. If that results
                # in a win for them, that is a lose for us
                _, winner = self.other.best_move(test_board, depth - 1)
                if winner == self.player:
                    # print(f"Win: other player lost so {self.player} should play {move}")
                    return move, winner
                elif winner == self.other.player:
                    # print(f"Lose: other player won so {self.player} should not play {move}")
                    continue
                else:
                    draw = move
                    continue
        
        # if we get to here, there are no winning moves. Aim
        # for a draw
        if draw >= 0:
            return draw, -1
        
        # If there is nothing to do but lose, do so
        return possible_moves[0], self.other.player



if __name__ == "__main__":

    from play import play_game
    from connect4 import Connect4
    from human_player import HumanPlayer

    grid = [
        [-1,  0,  0, -1, -1,  1,  1],
        [-1,  0,  0, -1, -1, -1,  1],
        [ 0,  0,  0,  0,  1,  1,  1],
        [ 0,  0,  0,  0,  0,  0, -1],
        [ 0,  0,  0,  0,  0,  0,  1],
        [ 0,  0,  0,  0,  0,  0,  1]]

    game = Connect4(grid)
    play_game(HumanPlayer(), CleverPlayer(game, 1, 4), game)
