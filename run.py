import random
from termcolor import colored
from utilis import clear_console


LENGTH_OF_BATTLESHIPS = [2, 3, 3, 4, 5]
PLAYER_GAME_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_GAME_BOARD = [[" "] * 8 for x in range(8)]
PLAYER_GUESS_GAME_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_GUESS_GAME_BOARD = [[" "] * 8 for x in range(8)]
LETTERS_TO_NUMBERS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                      'H': 7}


def starting_menu():
    """
    Opening screen to the game
    """
    clear_console()
    print(
        """
        _ _ _ ____ _    ____ ____ _  _ ____    ___ ____ 
        | | | |___ |    |    |  | |\/| |___     |  |  | 
        |_|_| |___ |___ |___ |__| |  | |___     |  |__|\n 
          ___  ____ ___ ___ _    ____ ____ _  _ _ ___  
          |__] |__|  |   |  |    |___ [__  |__| | |__] 
          |__] |  |  |   |  |___ |___ ___] |  | | |   \n      
        """
    )
    print(
        """
        
        """
    )
    while True:
        try:
            instruction = input(
                colored(
                    "Type p to play or i for instructions and press Enter:\n",
                    "blue"
                )
            ).upper()
            # if its i give the instructions
            if instruction == "I":
                print(
                    colored(
                        """
    1. Place your ships on the board:
        - You will be told the size of the ship you have to place
        (there are 5 in total).
        - You will then be asked for a direction to place your your
        ship (H for Horizontal or V for Vertical).
        - You will then asked for a starting point this is a point on the
        board that the ship starts at. You select this point with a
        number (1 - 8) and a letter (A - H), which represent the x
        and the y axis respectively.
        - The ship will start at the starting point and will take up
        the size of the ship in direction input.
    2. Attack the computers side of the board. You can attack the
        computer by using the coordinates similar to placing your
        ships. An x represents a hit and an - represents a miss.
    3. The game is won when a player get 17 hits on their opponents
        board
    4. Remember, you are always allowed to quit the game by pressing 'Q'
        your progress will not be saved.\n""",
                        "yellow",
                    )
                )
            elif instruction == "P":
                break
            else:
                raise ValueError()
        except (AttributeError, ValueError):
            print(
                colored(
                    "Please type p to play or i for instructions and press Enter",
                    "red"
                )
            )
    clear_console()


def create_user():
    name = input(colored("Please give your username:\n", "green"))


def print_game_board(game_board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for board_row in game_board:
        print("%d|%s" % (row_number, "|".join(board_row)))
        row_number += 1


def place_battleships(game_board):
    for battleship_length in LENGTH_OF_BATTLESHIPS:
        while True:
            if game_board == COMPUTER_GAME_BOARD:
                board_orientation, board_row, board_column = random.choice(["H", "V"]), random.randint(0, 7), random.randint(0, 7)
                if check_if_battleship_fits(battleship_length, board_row, board_column, board_orientation):
                    if check_if_battleship_overlaps(game_board, board_row, board_column, board_orientation, battleship_length) == False:
                        if board_orientation == "H":
                            for i in range(board_column, board_column + battleship_length):
                                game_board[board_row][i] = "X"
                        else:
                            for i in range(board_row, board_row + battleship_length):
                                game_board[i][board_column] = "X"
                        break
            else:
                place_battleships = True
                print('Place your ship with a length of ' + str(battleship_length))
                board_row, board_column, board_orientation = user_input(place_battleships)
                if check_if_battleship_fits(battleship_length, board_row, board_column, board_orientation):
                    if check_if_battleship_overlaps(game_board, board_row, board_column, board_orientation, battleship_length) == False:
                        if board_orientation == "H":
                            for i in range(board_column, board_column +
                                           battleship_length):
                                game_board[board_row][i] = "X"
                        else:
                            for i in range(board_row, board_row +
                                           battleship_length):
                                game_board[i][board_column] = "X"
                    else:
                        print("You already have a ship in this location,\
                               please try again.")
                        break


def check_if_battleship_fits(BATTLESHIP_LENGTH, board_row, board_column, board_orientation):
    if board_orientation == "H":
        if board_column + BATTLESHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if board_row + BATTLESHIP_LENGTH > 8:
            return False
        else:
            return True


def check_if_battleship_overlaps(game_board, board_row, board_column, board_orientation, battleship_length):
    if board_orientation == "H":
        for i in range(board_column, board_column + battleship_length):
            if game_board[board_row][i] == "X":
                return True
    else:
        for i in range(board_row, board_row + battleship_length):
            if game_board[i][board_column] == "X":
                return True
    return False


def user_input(place_battleships):
    if place_battleships == True:
        while True:
            try:
                board_orientation = input("Enter orientation, Key: H = Horizontal | V = Vertical (H or V) or Q to quit: ").upper()
                if board_orientation == 'Q':
                    print(f"You have quit the game.")
                    print("Hope you come back soon!")
                return 'Q'
                if board_orientation == "H" or board_orientation == "V":
                    break
            except TypeError:
                print('Please enter a valid orientation, either H or V or Q to quit: ')
        while True:
            try:
                board_row = input("Enter the number for the row you want to place your ship on: ")
                if board_orientation == 'Q':
                    print(f"You have quit the game.")
                    print("Hope you come back soon!")
                return 'Q'
                if board_row in '12345678':
                    board_row = int(board_row) - 1
                    break
            except ValueError:
                print('Please enter a valid number, between 1 and 8 or Q to quit: ')
        while True:
            try:
                board_column = input("Enter the letter for the column you want to place your ship on: ").upper()
                if board_orientation == 'Q':
                    print(f"You have quit the game.")
                    print("Hope you come back soon!")
                return 'Q'
                if board_column in 'ABCDEFGH':
                    board_column = LETTERS_TO_NUMBERS[board_column]
                    break
            except KeyError:
                print('Please enter a valid letter, between A and H or Q to quit: ')
        return board_row, board_column, board_orientation
    else:
        while True:
            try:
                board_row = input("Please enter the number for the row you want attack: ")
                if board_orientation == 'Q':
                    print(f"You have quit the game.")
                    print("Hope you come back soon!")
                return 'Q'
                if board_row in '12345678':
                    board_row = int(board_row) - 1
                    break
            except ValueError:
                print('Please enter a valid number, between 1 and 8')
        while True:
            try:
                board_column = input("Enter the letter for the column you want to attack: ").upper()
                if board_orientation == 'Q':
                    print(f"You have quit the game.")
                    print("Hope you come back soon!")
                return 'Q'
                if board_column in 'ABCDEFGH':
                    board_column = LETTERS_TO_NUMBERS[board_column]
                    break
            except KeyError:
                print('Please enter a valid letter, between A and H')
        return board_row, board_column


def count_hit_battleships(game_board):
    count = 0
    for battleship_row in game_board:
        for battleship_column in battleship_row:
            if battleship_column == 'X':
                count += 1
    return count


def turn(game_board):
    if game_board == PLAYER_GUESS_GAME_BOARD:
        board_row, board_column = user_input(PLAYER_GUESS_GAME_BOARD)
        if game_board[board_row][board_column] == "-":
            turn(game_board)
        elif game_board[board_row][board_column] == "X":
            turn(game_board)
        elif COMPUTER_GAME_BOARD[board_row][board_column] == "X":
            game_board[board_row][board_column] == "X"
        else:
            game_board[board_row][board_column] = "-"
    else:
        board_row, board_column = random.randint(0, 7), random.randint(0, 7)
        if game_board[board_row][board_column] == "-":
            turn(game_board)
        elif game_board[board_row][board_column] == "X":
            turn(game_board)
        elif PLAYER_GAME_BOARD[board_row][board_column] == "X":
            game_board[board_row][board_column] == "X"
        else:
            game_board[board_row][board_column] = "-"


starting_menu()
create_user()
place_battleships(COMPUTER_GAME_BOARD)
print_game_board(COMPUTER_GUESS_GAME_BOARD)
print_game_board(PLAYER_GAME_BOARD)
place_battleships(PLAYER_GAME_BOARD)

while True:
    while True:   
        print('Guess the computers battleships location!')
        print_game_board(PLAYER_GUESS_GAME_BOARD)
        turn(PLAYER_GUESS_GAME_BOARD)
        break
    if count_hit_battleships(PLAYER_GUESS_GAME_BOARD) == 17:
        print("Congratulations! You win.")
        break
    while True:
        turn(COMPUTER_GUESS_GAME_BOARD)
        break
    print_game_board(COMPUTER_GUESS_GAME_BOARD)
    if count_hit_battleships(COMPUTER_GUESS_GAME_BOARD) == 17:
        print("Oh no! The computer has sunk all of your ships, you lose!")
        break
