from flask import Flask, Response, render_template, request
from tictactoe.model.tic_tac_toe_model import TicTacToeModel


class EndpointAction:
    """EndpointAction enables adding routes without annotations."""

    def __init__(self, action):
        self.action = action

    def __call__(self, *args):
        # Perform the action
        answer = self.action()
        # Create the answer (bundle it in a correctly formatted HTTP answer)
        self.response = Response(answer, status=200, headers={})
        # Send it
        return self.response


class TicTacToeGameController:
    """The tic-tac-toe game controller."""

    app = None
    model = None
    anweisung_text = ""
    meldung_text = ""
    images = [[]]

    def __init__(self, name, image_path="/images"):
        self.app = Flask(
            name,
            static_url_path="",
            static_folder=image_path,
            template_folder="tictactoe/flask/templates",
        )
        self.model = TicTacToeModel()
        self.images = [[0] * 3 for _ in range(3)]
        self.add_all_endpoints()

    def get_app(self):
        return self.app

    def run(self):
        """Run the flask App."""
        self.app.run(debug=True, use_reloader=False)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, **options):
        """Add an endpoint/route to the controller."""
        self.app.add_url_rule(
            endpoint, endpoint_name, EndpointAction(handler), **options
        )

    def add_all_endpoints(self):
        """Add all endpoints/routes to the controller."""
        # Add root endpoint
        self.add_endpoint(
            endpoint="/",
            endpoint_name="/",
            handler=self.tic_tac_toe_game,
            methods=["GET"],
        )

        # Add action endpoints
        self.add_endpoint(
            endpoint="/take_coordinates",
            endpoint_name="/take_coordinates",
            handler=self.take_coordinates,
            methods=["POST"],
        )

    def get_model(self):
        """Get the model."""
        return self.model

    def tic_tac_toe_game(self):
        """Render the HTML template."""
        return render_template(
            "tic_tac_toe_flask_view.html",
            anweisungen=self.anweisung_text,
            meldungen=self.meldung_text,
            images=self.images,
        )

    def take_coordinates(self):
        """Take coordinates x/y for active player when button is pressed."""
        x = int(request.form.get("a"))
        y = int(request.form.get("b"))
        if not self.get_model().game_won():
            if self.get_model().coordinates_taken(x, y):
                self.anweisung_text = (
                    "Koordinaten "
                    + str(x)
                    + " "
                    + str(y)
                    + " sind schon belegt! "
                    + "Wähle andere Koordinaten "
                )

            else:
                self.anweisung_text = ""
                self.get_model().set_mark(x, y)
                sign = self.get_model().get_active_player_sign()
                if sign == self.get_model().player_one_sign:
                    filename = 1
                else:
                    filename = 2
                self.images[x][y] = filename

                if self.get_model().game_won():
                    self.congratulate_player(
                        self.get_model().get_active_player_name())
                else:
                    self.get_model().switch_player()

        return render_template(
            "tic_tac_toe_flask_view.html",
            anweisungen=self.anweisung_text,
            meldungen=self.meldung_text,
            images=self.images,
        )

    def congratulate_player(self, active_player):
        """Prepare congratulation message."""
        self.meldung_text = "Herzlichen Glückwunsch Spieler " + active_player + " !"
