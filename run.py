import random


LENGTH_OF_BATTLESHIPS = [2, 3, 3, 4, 5]
PLAYER_GAME_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_GAME_BOARD = [[" "] * 8 for x in range(8)]
PLAYER_GUESS_GAME_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_GUESS_GAME_BOARD = [[" "] * 8 for x in range(8)]
LETTERS_TO_NUMBERS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                      'H': 7}


def print_game_board(game_board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in game_board:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1


def place_battleships(game_board):
    for battleship_length in LENGTH_OF_BATTLESHIPS:
        while True:
            if game_board == COMPUTER_GAME_BOARD:
                board_orientation, board_row, board_column = random.choice(["H", "V"]), random.randint(0, 7), random.randint(0, 7)
                if check_if_battleship_fits(battleship_length, board_row, board_column, board_orientation):
                    if check_if_battleship_overlaps(game_board, board_row, board_column, board_orientation, battleship_length) == False:
                        if board_orientation == "H":
                            for x in range(board_column, board_column + battleship_length):
                                game_board[board_row][x] = "X"
                        else:
                            for x in range(board_row, board_row + battleship_length):
                                game_board[x][board_column] = "X"
                        break
            else:
                place_battleships = True
                print('Place your ship with a length of ' + str(battleship_length))
                board_row, board_column, board_orientation = user_input(place_battleships)
                if check_if_battleship_fits(board_row, board_column, board_orientation, battleship_length):
                    if check_if_battleship_overlaps(game_board, board_row, board_column, board_orientation, battleship_length) == False:
                        if board_orientation == "H":
                            for x in range(board_column, board_column + battleship_length):
                                game_board[board_row][x] = "X"
                        else:
                            for x in range(board_row, board_row + battleship_length):
                                game_board[x][board_column] = "X"
                        break


def check_if_battleship_fits(battleship_length, board_row, board_column, board_orientation):
    if board_orientation == "H":
        if board_column + battleship_length > 8:
            return False
        else:
            return True
    else:
        if board_row + battleship_length > 8:
            return False
        else:
            return True


def check_if_battleship_overlaps(game_board, board_row, board_column, board_orientation, battleship_length):
    if board_orientation == "H":
        for x in range(board_column, board_column + battleship_length):
            if game_board[board_row][x] == "X":
                return True
    else:
        for x in range(board_row, board_row + battleship_length):
            if game_board[x][board_column] == "X":
                return True


def user_input(place_battleships):
    if place_battleships == True:
        while True:
            try:
                board_orientation = input("Enter orientation, Key: H = Horizontal | V = Vertical (H or V): ").upper()
                if board_orientation == "H" or board_orientation == "V":
                    break
            except TypeError:
                print('Please enter a valid orientation, either H or V')
        while True:
            try:
                board_row = input("Enter the number for the row you want to place your ship on: ")
                if board_row in '12345678':
                    board_row = int(board_row) - 1
                    break
            except ValueError:
                print('Please enter a valid number, between 1 and 8')
        while True:
            try:
                board_column = input("Enter the letter for the column you want to place your ship on: ")
                if board_column in 'ABCDEFGH':
                    board_column = LETTERS_TO_NUMBERS[board_column]
                    break
            except KeyError:
                print('Please enter a valid letter, between A and H')
        return board_row, board_column, board_orientation
    else:
        while True:
            try:
                board_row = input("Please enter the number for the row you want attack: ")
                if board_row in '12345678':
                    board_row = int(board_row) - 1
                    break
            except ValueError:
                print('Please enter a valid number, between 1 and 8')
        while True:
            try:
                board_column = input("Enter the letter for the column you want to attack: ")
                if board_column in 'ABCDEFGH':
                    board_column = LETTERS_TO_NUMBERS[board_column]
                    break
            except KeyError:
                print('Please enter a valid letter, between A and H')
        return board_row, board_column


def count_hit_battleships(game_board):
    pass
    count = 0
    for battleship_row in game_board:
        for battleship_column in battleship_row:
            if battleship_column == 'X':
                count += 1
    return count


def turn(game_board):
    if game_board == PLAYER_GUESS_GAME_BOARD:
        battleship_row, battleship_column = user_input(PLAYER_GUESS_GAME_BOARD)
        if game_board[battleship_row][battleship_column] == "-":
            turn(game_board)
        elif game_board[battleship_row][battleship_column] == "X":
            turn(game_board)
        elif COMPUTER_GAME_BOARD[battleship_row][battleship_column] == "X":
            game_board[battleship_row][battleship_column] == "X"
        else:
            game_board[battleship_row][battleship_column] = "-"
    else:
        battleship_row, battleship_column = random.randint(0, 7), random.randint(0, 7)
        if game_board[battleship_row][battleship_column] == "-":
            turn(game_board)
        elif game_board[battleship_row][battleship_column] == "X":
            turn(game_board)
        elif PLAYER_GAME_BOARD[battleship_row][battleship_column] == "X":
            game_board[battleship_row][battleship_column] == "X"
        else:
            game_board[battleship_row][battleship_column] = "-"


place_battleships(COMPUTER_GAME_BOARD)
print_game_board(COMPUTER_GAME_BOARD)
print_game_board(PLAYER_GAME_BOARD)
place_battleships(PLAYER_GAME_BOARD)

while True:
    while True:
        print('Guess the computers battleships location!')
        print_game_board(PLAYER_GAME_BOARD)
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
