Feature: Create Game Model
    A model that determines when the game is won, whose turn it is and what the current status is

    Scenario: Making a valid not winning move
        Given The game is started
        And Player two needs only coordinates 1 1 to win
        And Player one has to move

        When A player makes a move to coordinates 1 1

        Then Player two is active
        And The game is not won

    Scenario: Making a valid winning move for player one
        Given The game is started
        And Player one needs only coordinates 1 1 to win
        And Player one has to move

        When A player makes a move to coordinates 1 1

        Then Player one is active
        And The game is won


    Scenario: Making a valid winning move for player two
        Given The game is started
        And Player two needs only coordinates 1 1 to win
        And Player two has to move

        When A player makes a move to coordinates 1 1

        Then Player two is active
        And The game is won
