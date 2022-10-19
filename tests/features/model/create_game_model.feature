Feature: Create Game Model
    A model that determines when the game is won, whose turn it is and what the current status is

    Scenario: No Coordinates are taken when game is started
        Given The game is started
        Then Coordinates 0 0 are not taken
        Then Coordinates 0 1 are not taken
        Then Coordinates 0 2 are not taken
        Then Coordinates 1 0 are not taken
        Then Coordinates 1 1 are not taken
        Then Coordinates 1 2 are not taken
        Then Coordinates 2 0 are not taken
        Then Coordinates 2 1 are not taken
        Then Coordinates 2 2 are not taken

    Scenario: Coordinates are taken after player takes them
        Given The game is started
        When A player makes a move to coordinates 1 1
        Then Coordinates 1 1 are taken

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

