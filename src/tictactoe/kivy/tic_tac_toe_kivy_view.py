import kivy.resources
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty


class TicTacToeKivyView(App):
    """The tic-tac-toe Kivy view."""

    controller = ObjectProperty()

    def __init__(self, image_path, controller):
        super(TicTacToeKivyView, self).__init__()
        self.controller = controller
        kivy.resources.resource_add_path(image_path)

    def build(self):
        """Initialize some variables."""
        self.title = "TicTacToe"
        self.root = RootWidget()
        self.root.controller = self.controller
        return self.root

    def set_error(self, text):
        """Display error message."""
        self.root.footer_text = text

    def set_coordinates_to(self, x, y, mark_filename):
        """Set players mark on coordinates."""
        getattr(self.root.ids, str(x) + "_" + str(y)).source = (
            mark_filename + ".png"
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
