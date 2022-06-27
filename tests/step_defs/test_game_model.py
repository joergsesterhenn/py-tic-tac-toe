from pytest_bdd import scenarios, given, when, then
from tictactoe.model.tic_tac_toe_model import TicTacToeModel

scenarios('../features')


@given("The game is started", target_fixture="game_model")
def my_game_model():
    model = TicTacToeModel()
    return model

@given("Player one needs only coordinates 1 1 to win", target_fixture="game_model")
def coordinates_not_taken(game_model):
    game_model.data[1][1] = ' '
    game_model.data[0][1] = 'o'
    game_model.data[2][1] = 'o'
    return game_model


@given("Player two needs only coordinates 1 1 to win", target_fixture="game_model")
def coordinates_not_taken(game_model):
    game_model.data[1][1] = ' '
    game_model.data[0][1] = 'x'
    game_model.data[2][1] = 'x'
    return game_model


@given("Player one has to move", target_fixture="game_model")
def player_ones_turn(game_model):
    game_model.active_player = "eins"
    return game_model

@given("Player two has to move", target_fixture="game_model")
def player_ones_turn(game_model):
    game_model.active_player = "zwei"
    return game_model

@when("A player makes a move to coordinates 1 1", target_fixture="game_model")
def move(game_model):
    game_model.set_mark(1, 1)
    if not game_model.game_won():
        game_model.switch_player()
    return game_model


@then("The game is won")
def is_won(game_model):
    assert game_model.game_won() is True


@then("The game is not won")
def is_not_won(game_model):
    assert game_model.game_won() is False


@then("Player one is active")
def one_active(game_model):
    assert game_model.get_active_player_name() == "eins"


@then("Player two is active")
def two_active(game_model):
    assert game_model.get_active_player_name() == "zwei"
