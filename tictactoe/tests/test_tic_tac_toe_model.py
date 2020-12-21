import unittest
from tictactoe.tic_tac_toe_model import TicTacToeModel


class TicTacToeModelTest(unittest.TestCase):

    cut = TicTacToeModel()

    def test_switch_player(self):
        self.cut.active_player = "eins"
        self.cut.switch_player()
        actual_player = self.cut.active_player
        expected_player = "zwei"
        self.assertEqual(actual_player, expected_player)


if __name__ == "__main__":
    unittest.main()
