from random import randint

HIDDEN_GAME_BOARD = [[' '] * 8 for x in range(8)]
GUESS_GAME_BOARD = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                      'H': 7}


def print_game_board(game_board):
    print('  A B C D E F G H')
    print('  ---------------')
    row_number = 1
    for row in game_board:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1


def create_battleships(game_board):
    for battleship in range(5):
        battleship_row, battleship_column = randint(0, 7), randint(0, 7)
        while game_board[battleship_row][battleship_column] == 'X':
            battleship_row, battleship_column = randint(0, 7), randint(0, 7)
        game_board[battleship_row][battleship_column] = 'X'


def get_location_of_battleship():
    board_row = input('Please enter a ship row 1-8')
    while board_row not in '12345678':
        print('Please enter a valid row')
        board_row = input('Please enter a ship row 1-8')
    board_column = input('Please enter a ship column A-H').upper()
    while board_column not in 'ABCDEFGH':
        print('Please enter a valid column')
        board_column = input('Please enter a ship column A-H').upper()
    return int(board_row) - 1, letters_to_numbers[board_column]


def count_hit_battleships(game_board):
    count = 0
    for battleship_row in game_board:
        for battleship_column in battleship_row:
            if battleship_column == 'X':
                count += 1
    return count

create_battleships()
turns = 10
# while turns > 0:
