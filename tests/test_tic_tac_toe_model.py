import unittest
from tictactoe.model.tic_tac_toe_model import TicTacToeModel


class TicTacToeModelTest(unittest.TestCase):
    """Test the model."""

    cut = TicTacToeModel()

    def test_switch_player(self):
        """Test if player was correctly switched."""
        self.cut.active_player = "eins"
        self.cut.switch_player()
        actual_player = self.cut.active_player
        expected_player = "zwei"
        self.assertEqual(actual_player, expected_player)


if __name__ == "__main__":
    unittest.main()
