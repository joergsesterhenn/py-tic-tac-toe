from tictactoe.tic_tac_toe_model import TicTacToeModel
from tic_tac_toe_kivy_view import TicTacToeKivyView


class TicTacToeGameController:
    """The tic-tac-toe game controller."""

    def __init__(self):
        self.model = TicTacToeModel()
        self.view = TicTacToeKivyView()
        self.view.controller = self

    def run_tic_tac_toe(self):
        self.view.run()

    def take_coordinates(self, x, y):
        """gets called when button is pressed to select coordinates."""
        if not self.model.check_won():
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
                self.view.set_coordinates_to(x, y, self.model.active_player)
                if self.model.check_won():
                    self.view.congratulate_player(self.model.active_player)
                else:
                    self.model.switch_player()
                    self.view.set_player(self.model.active_player)


controller = TicTacToeGameController()
controller.run_tic_tac_toe()
