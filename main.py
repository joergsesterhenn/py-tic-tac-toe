import os


def check_won(data):
    return (data[0][0] + data[1][0] + data[2][0] == player_one_sign + player_one_sign + player_one_sign or
            data[0][1] + data[1][1] + data[2][1] == player_one_sign + player_one_sign + player_one_sign or
            data[0][2] + data[1][2] + data[2][2] == player_one_sign + player_one_sign + player_one_sign or

            data[0][0] + data[0][1] + data[0][2] == player_one_sign + player_one_sign + player_one_sign or
            data[1][0] + data[1][1] + data[1][2] == player_one_sign + player_one_sign + player_one_sign or
            data[2][0] + data[2][1] + data[2][2] == player_one_sign + player_one_sign + player_one_sign or

            data[0][0] + data[1][1] + data[2][2] == player_one_sign + player_one_sign + player_one_sign or
            data[0][2] + data[1][1] + data[2][0] == player_one_sign + player_one_sign + player_one_sign or

            data[0][0] + data[1][0] + data[2][0] == player_two_sign + player_two_sign + player_two_sign or
            data[0][1] + data[1][1] + data[2][1] == player_two_sign + player_two_sign + player_two_sign or
            data[0][2] + data[1][2] + data[2][2] == player_two_sign + player_two_sign + player_two_sign or

            data[0][0] + data[0][1] + data[0][2] == player_two_sign + player_two_sign + player_two_sign or
            data[1][0] + data[1][1] + data[1][2] == player_two_sign + player_two_sign + player_two_sign or
            data[2][0] + data[2][1] + data[2][2] == player_two_sign + player_two_sign + player_two_sign or

            data[0][0] + data[1][1] + data[2][2] == player_two_sign + player_two_sign + player_two_sign or
            data[0][2] + data[1][1] + data[2][0] == player_two_sign + player_two_sign + player_two_sign)


def switch_player(name):
    if name == "eins":
        return "zwei"
    else:
        return "eins"


def print_tic_tac_toe_field(data):
    os.system('cls')
    print("""###################################################
            T I C    T A C    T O E
###################################################
                 |¯¯¯|¯¯¯|¯¯¯|
                 | """ + data[0][0] + """ | """ + data[1][0] + """ | """ + data[2][0] + """ |
                 |---|---|---|
                 | """ + data[0][1] + """ | """ + data[1][1] + """ | """ + data[2][1] + """ |
                 |---|---|---|
                 | """ + data[0][2] + """ | """ + data[1][2] + """ | """ + data[2][2] + """ |
                 |___|___|___|
###################################################""")


tic_tac_toe_data = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player_one_sign = "o"
player_two_sign = "x"
spieler = "eins"
won = False
inputtext = ""
errortext = ""


def is_not_valid(text):
    return not (len(text) == 3 and text[0] in ("0", "1", "2") and text[1] == " " and text[2] in ("0", "1", "2"))


def coordinates_taken(a, b):
    return tic_tac_toe_data[a][b] != " "


while not won:
    print_tic_tac_toe_field(tic_tac_toe_data)
    if errortext != "":
        print(f'{errortext}')
    inputtext = input(f'Player {spieler}, bitte wähle x→ und y↓ Koordinaten (Werte 0 bis 2): ')
    errortext = ""
    if is_not_valid(inputtext):
        errortext = "Ungültige Eingabe " + inputtext + "! Ein gültiger Eingabewert ist z.B.: 1 1 "
        continue

    x, y = map(int, inputtext.split())
    if coordinates_taken(x, y):
        errortext = "Koordinaten "+str(x)+" "+str(y)+" sind schon belegt! Wähle andere Koordinaten "
        continue

    if spieler == "eins":
        tic_tac_toe_data[x][y] = player_one_sign
    else:
        tic_tac_toe_data[x][y] = player_two_sign
    won = check_won(tic_tac_toe_data)
    if won:
        print_tic_tac_toe_field(tic_tac_toe_data)
        print(f'Gratulation Spieler {spieler} du hast gewonnen!')
        print('###################################################')
    spieler = switch_player(spieler)
