# ----- Global Variables -----

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_is_going = True

# Who is the winner? Is it tie?
winner = None

# Who is the current player
current_player = "X"


# Display a board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# Play a game Tic-Tac-Toe
def play_game():
    # Display initial board
    display_board()

    # While the game is still going
    while game_is_going:
        # Handle a single turn of a player
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip  to the other player
        flip_player()

    # The game is over
    if winner == None:
        print("The game is over. It is tie!")
    else:
        print("The game is over. The winner is " + winner + ".")


# Handle a single turn of a player
def handle_turn(player):
    print(player + " is playing.")
    position = input("Enter the position from 1 to 9: ")

    valid = False
    while not valid:

        while position not in list(map(str, range(1, 10))):
            position = input("Enter the position from 1 to 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("The position is not empty. Go again.")

    board[position] = player
    display_board()


# Check if the game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# Check for the winner
def check_for_winner():
    # Set up global variable
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return winner


# Check if tie
def check_if_tie():
    # Set up global variable
    global game_is_going

    if "-" not in board:
        game_is_going = False


# Check rows
def check_rows():
    # Set up global variable
    global game_is_going

    # Check if any of the rows have all the same values (not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row has a match the game is over
    if row_1 or row_2 or row_3:
        game_is_going = False
    # return the winner: X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


# Check columns
def check_columns():
    # Set up global variable
    global game_is_going

    # Check if any of the columns have all the same values (not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any column has a match the game is over
    if column_1 or column_2 or column_3:
        game_is_going = False
    # return the winner: X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]


# Check diagonals
def check_diagonals():
    # Set up global variable
    global game_is_going

    # Check if any of the diagonals have all the same values (not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any diagonal has a match the game is over
    if diagonal_1 or diagonal_2:
        game_is_going = False
    # return the winner: X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]


# Flip  to the other player
def flip_player():
    # Set up global variable
    global current_player

    if current_player == "X":
        current_player = "0"
    elif current_player == "0":
        current_player = "X"


play_game()
