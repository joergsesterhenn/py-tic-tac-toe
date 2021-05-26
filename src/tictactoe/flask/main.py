import os

from tictactoe.flask.tic_tac_toe_game_controller import TicTacToeGameController


def run():
    """Run the flask App."""
    image_path = os.path.abspath("images")
    controller = TicTacToeGameController("TicTacToe", image_path)
    controller.run()

