from tictactoe.tic_tac_toe_model import TicTacToeModel
from ascii.tic_tac_toe_cli_view import TicTacToeCLIView


class TicTacToeGameController:
    """The tic-tac-toe game controller."""

    def __init__(self):
        self.model = TicTacToeModel()
        self.view = TicTacToeCLIView()

    def run_tic_tac_toe(self):
        while not self.model.check_won():
            x, y = self.view.get_player_input(self.model.active_player, self.model.get_data())
            if self.model.coordinates_taken(x, y):
                self.view.set_error("Koordinaten " + str(x) + " " + str(y) +
                                    " sind schon belegt! Wähle andere Koordinaten ")
                continue
            self.model.set_mark(x, y)
            if self.model.check_won():
                self.view.congratulate_player(self.model.active_player, self.model.get_data())
            self.model.switch_player()


controller = TicTacToeGameController()
controller.run_tic_tac_toe()
