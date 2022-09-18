#Legend 
# X for placing the battleship and for hitting the battleship
# ' ' for available space 
# '-'for missed shot 


from random import randint

HIDDEN_BOARD = [[''] * 8 for x in range(8)]
GUESS_BOARD = [[''] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def print_board(board):
    print('    A B C D E F G H')
    print('    ---------------') 
    row_numbers = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

#computer creates 5 ships 
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
            board[ship_row][ship_column] = 'X'
            
    

def get_ship_location():"%d|%s|" % (row_number, "|".join(row))


def count_hit_ships():
    pass

create_ships()
print_board(board)
turns = 10
while turns > 0:
    pass
