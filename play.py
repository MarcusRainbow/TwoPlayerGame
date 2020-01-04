from player import Player
from game import Game
from board import Board

def play_game(player1: Player, player2: Player, game: Game):
    """
    Plays a game, where the game and players are supplied
    """

    # start with a clean board
    board = game.clean_board()
    tokens = game.tokens()

    # take turns making moves
    # try:
    while True:
        move1 = player1.next_move(board)
        board.apply_move(move1, tokens[0])
        winner = game.test_win(board)
        if winner >= 0:
            break
        move2 = player2.next_move(board)
        board.apply_move(move2, tokens[1])
        winner = game.test_win(board)
        if winner >= 0:
            break
    # except Exception as e:
    #     print(e)
    #     return

    if winner == 0:
        print("You win!")
    else:
        print("Computer wins!")
