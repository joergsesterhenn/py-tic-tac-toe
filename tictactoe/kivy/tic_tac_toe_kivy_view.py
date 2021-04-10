from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder


class TicTacToeKivyView(App):
    """The tic-tac-toe Kivy view."""

    controller = ObjectProperty()

    def build(self):
        """Initialize some variables."""
        self.root = ""
        self.title = "TicTacToe"
        self.root = root = RootWidget()
        self.root.controller = self.controller
        return root

    def set_error(self, text):
        """Display error message."""
        self.root.footer_text = text

    def set_coordinates_to(self, x, y, player):
        """Set players mark on coordinates."""
        getattr(self.root.ids, str(x) + "_" + str(y)).source = (
            "images/" + player + ".png"
        )

    def set_player(self, player):
        """Set current player."""
        self.root.input_text = "Spieler " + player + " wähle ein Feld"

    def congratulate_player(self, player):
        """Congratulate player who won."""
        self.root.input_text = "Spieler " + player + " hat gewonnen!"
        self.root.footer_text = "Herzlichen Glückwunsch!"


class RootWidget(BoxLayout):
    """The root widget of the app."""
    footer_text = StringProperty()
    input_text = StringProperty()


Builder.load_file("mainview.kv")
