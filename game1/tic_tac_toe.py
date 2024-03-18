# Let's start by initializing our game1 board
table = ["?", "?", "?",
         "?", "?", "?",
         "?", "?", "?"]

# Know if game1 is still going on by setting it to True
run = True

# Initialize our current player to be X
current_player = "X"

# Function to display our game1 board
def display_table():
    print(table[0] + " | " + table[1] + " | " + table[2] + "      " + "1|2|3")
    print(table[3] + " | " + table[4] + " | " + table[5] + "      " + "4|5|6")
    print(table[6] + " | " + table[7] + " | " + table[8] + "      " + "7|8|9")

# Funtion to define players
def players():
    print("Select Player - X or O")
    player1 = input("Player1: ")
    player2 = ""
    if player1 == "X":
        player2 = "O"
        print("Player2: " + player2)
    elif player1 == "O":
        player2 = "X"
        print("Player2: " + player2)
    elif player1 != "O" or player1 != "X":
        print("Sorry,invalid input. Type X or O")
        play_game()

# Define the player position
def player_position():
    global run
    print("Current Player: " + current_player)
    position = input("Choose position (1-9): ")

    # Loop through the program untill there is a win or tie
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose position (1-9): ")
        position = int(position) - 1

        if table[position] == "-":
            valid = True
        else:
            print("Position is taken, choose another position!")
    table[position] = current_player
    display_table()

# Function to play our tic tac game1
def play_game():
    print("My Tic Tac Toe Game")
    display_table()
    players()

    # loop  to flip players untill there is a win
    while run:
        player_position()

        # Check winner
        def check_winner():
            global run
            # Check rows if there is a win
            if table[0] == table[1] == table[2] != "-":
                run = False
                print(f"{table[0]} WON!")
            elif table[3] == table[4] == table[5] != "-":
                run = False
                print(f"{table[3]} WON!")
            elif table[6] == table[7] == table[8] != "-":
                run = False
                print(f"{table[6]} WON!")
            # Check columns if there is a win
            elif table[0] == table[3] == table[6] != "-":
                run = False
                print(f"{table[0]} WON!")
            elif table[1] == table[4] == table[7] != "-":
                run = False
                print(f"{table[1]} WON!")
            elif table[2] == table[5] == table[8] != "-":
                run = False
                print(f"{table[2]} WON!")
            # Check diagonals if there is a win
            elif table[0] == table[4] == table[8] != "-":
                run = False
                print(f"{table[0]} WON!")
            elif table[2] == table[4] == table[6] != "-":
                run = False
                print(f"{table[6]} WON!")
            # If none of the above, then, it's a tie
            elif "-" not in table:
                run = False
                print("It's a Tie")
                exit()

        # Function to flip player
        def flip_player():
            global current_player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        flip_player()
        check_winner()


# Play our tic tac game1
play_game()