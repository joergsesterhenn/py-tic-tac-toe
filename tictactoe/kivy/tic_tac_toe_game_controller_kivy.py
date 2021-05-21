from tic_tac_toe_kivy_view import TicTacToeKivyView
from tictactoe.tic_tac_toe_model import TicTacToeModel


class TicTacToeGameController:
    """The tic-tac-toe game controller."""

    def __init__(self):
        self.model = TicTacToeModel()
        self.view = TicTacToeKivyView()
        self.view.controller = self

    def run_tic_tac_toe(self):
        """Run the game."""
        self.view.run()

    def take_coordinates(self, x, y):
        """Take coordinates x/y for active player when button is pressed."""
        if not self.model.game_won():
            if self.model.coordinates_taken(x, y):
                self.view.set_error(
                    "Koordinaten "
                    + str(x)
                    + " "
                    + str(y)
                    + " sind schon belegt! Wähle andere Koordinaten "
                )
            else:
                self.view.set_error("")
                self.model.set_mark(x, y)
                if self.model.get_active_player_sign() == \
                        self.model.player_one_sign:
                    filename = str(1)
                else:
                    filename = str(2)
                self.view.set_coordinates_to(x, y, filename)
                if self.model.game_won():
                    self.view.congratulate_player(
                        self.model.get_active_player_name())
                else:
                    self.model.switch_player()
                    self.view.set_player(self.model.get_active_player_name())


controller = TicTacToeGameController()
controller.run_tic_tac_toe()
