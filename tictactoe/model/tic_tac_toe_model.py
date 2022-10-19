class TicTacToeModel:
    """The tic-tac-toe model."""

    initial_data = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player_one_sign = "o"
    player_two_sign = "x"

    def __init__(self):
        self.data = self.initial_data
        self.active_player = "eins"

    def set_mark(self, x_position, y_position):
        """Set a mark on position x/y for active player."""
        self.data[x_position][y_position] = self.get_active_player_sign()

    def get_data(self):
        """Return the current datamodel."""
        return self.data

    def get_active_player_name(self):
        """Get name of active player."""
        return self.active_player

    def get_active_player_sign(self):
        """Get sign of active player."""
        if self.active_player == "eins":
            return self.player_one_sign
        return self.player_two_sign

    def switch_player(self):
        """Switch the player."""
        if self.active_player == "eins":
            self.active_player = "zwei"
        else:
            self.active_player = "eins"

    def game_won(self):
        """Check if the game is won."""
        return (
            self.data[0][0] == self.data[1][0] == self.data[2][0]
            and self.coordinates_taken(2, 0)
            or self.data[0][1] == self.data[1][1] == self.data[2][1]
            and self.coordinates_taken(2, 1)
            or self.data[0][2] == self.data[1][2] == self.data[2][2]
            and self.coordinates_taken(2, 2)
            or self.data[0][0] == self.data[0][1] == self.data[0][2]
            and self.coordinates_taken(0, 2)
            or self.data[1][0] == self.data[1][1] == self.data[1][2]
            and self.coordinates_taken(1, 2)
            or self.data[2][0] == self.data[2][1] == self.data[2][2]
            and self.coordinates_taken(2, 2)
            or self.data[0][0] == self.data[1][1] == self.data[2][2]
            and self.coordinates_taken(2, 2)
            or self.data[0][2] == self.data[1][1] == self.data[2][0]
            and self.coordinates_taken(2, 0)
        )

    def coordinates_taken(self, a, b):
        """Check if coordinates are already taken."""
        return self.data[a][b] != " "
