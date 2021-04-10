def print_field(data):
    """Display current game."""
    print(
        """    ###################################################
                T I C    T A C    T O E
    ###################################################
                     |¯¯¯|¯¯¯|¯¯¯|
                     | """
        + data[0][0]
        + """ | """
        + data[1][0]
        + """ | """
        + data[2][0]
        + """ |
                     |---|---|---|
                     | """
        + data[0][1]
        + """ | """
        + data[1][1]
        + """ | """
        + data[2][1]
        + """ |
                     |---|---|---|
                     | """
        + data[0][2]
        + """ | """
        + data[1][2]
        + """ | """
        + data[2][2]
        + """ |
                     |___|___|___|
    ###################################################"""
    )


def is_not_valid(text):
    """Validate input text."""
    return not (
        len(text) == 3
        and text[0] in ("0", "1", "2")
        and text[1] == " "
        and text[2] in ("0", "1", "2")
    )


class TicTacToeCLIView:
    """The tic-tac-toe CLI view."""

    def __init__(self):
        self.error_text = ""
        self.input_text = ""

    def get_player_input(self, spieler, data):
        """Get input from player and validate."""
        valid_reply_received = False
        while not valid_reply_received:
            print_field(data)
            if self.error_text != "":
                print(f"      {self.error_text}")
            self.input_text = input(
                f"      Spieler {spieler}"
                f", bitte wähle x→ und y↓ Koordinaten (Werte 0 bis 2): "
            )
            self.error_text = ""
            if is_not_valid(self.input_text):
                self.error_text = (
                    "Ungültige Eingabe "
                    + self.input_text
                    + "! Ein gültiger Eingabewert ist z.B.: 1 1 "
                )
            else:
                valid_reply_received = True
        return map(int, self.input_text.split())

    @staticmethod
    def congratulate_player(spieler, data):
        """Congratulate player who won."""
        print_field(data)
        print(f"        Gratulation Spieler {spieler} du hast gewonnen!")
        print("    ###################################################")

    def set_error(self, error):
        """Display error message."""
        self.error_text = error
