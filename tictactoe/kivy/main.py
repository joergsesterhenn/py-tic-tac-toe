import os

from tictactoe.kivy.tic_tac_toe_game_controller import TicTacToeGameController


def run():
    """Run the kivy App."""
    image_path = os.path.abspath("images")
    controller = TicTacToeGameController(image_path)
    controller.run()
