# -*- coding: utf-8 -*-
import random

# Input welcome message with rules and display it.
name= input("Enter name:")
print("Welcome to Battleship Py! Build ships with: V for VERTICAL, H for HORIZONTAL, with cooordinates between A-J and 1-8. GOOD LUCK",name)


def guess_checker(guess):
    """
    Checks the guesses of both the computer and the player.
    """
    if (guess[0].upper() in x[0]) and (guess[1] in y[0]):
        return True
    else:
        print("*PLEASE ENTER A VALID COORDINATE!")
        return False


def viewer(matrix):
    """ 
     Builds the matrix that contains the game 10 x 10 grid for placement
    of ships using coordinates
    """
    for i in range(10):
        print(" " + x[0][i] + " ", end="")
    print()
    for i in range(10):
        print(" " + "—" + " ", end="")
    print()
    for a in range(10):
        for b in range(10):
            print(matrix[a][b], end="")
        print("|" + y[0][a], end="\n")


def direction_validity(occupying_area, x_cor, y_cor, direction):
    """
    
    """
    if direction == "v":
        if occupying_area <= 11 - y_cor:
            return True
        print(
            f"[Illegal move! Enter legal coordinates!]")
        return False

    elif direction == "h": 
        if occupying_area <= 11 - x_cor:
            return True
        return False


def is_occupied(occupying_area, x_cor, y_cor, direction):
    for i in range(1, occupying_area):

        if direction == "v":
            if grid[y_cor + i][x_cor] == " X ":
                print(
                    "Ship approaching with same coordinates!")
                return True
            else:
                continue

            return False
        elif direction == "h":
            if grid[y_cor][x_cor + i] == " X ":
                print(
                    "The enemy ship is there! Choose another!")
                return True
            else:
                continue


def opponent_occupied(occupying_area, x_cor, y_cor, direction):
    for i in range(0, occupying_area):

        if direction == "v":
            if opponent_grid[y_cor + i][x_cor] == " X ":
                print(
                    "There is already another ship intersecting with these coordinates!")
                return True
            else:
                continue

            return False
        elif direction == "h":
            if opponent_grid[y_cor][x_cor + i] == " X ":
                print(
                    "There is already another ship intersecting with these coordinates!")
                return True
            else:
                continue


def check(coordinate_ships):
    if ((len(coordinate_ships) == 3) and (
            coordinate_ships[0].lower() == "v" or coordinate_ships[0].lower() == "h") and (
            coordinate_ships[1].upper() in x[0]) and (coordinate_ships[2] in y[0])):
        return True
    else:
        print("*PLEASE ENTER A VALID COORDINATE!")
        return False


def input_processor(coordiante_ships):
    direction_ships = coordinate[0].lower()

    for ELEMENT in x[0]:

        if ELEMENT in coordinate[1:2].upper():
            x_cor = x[0].find(ELEMENT)

            break

    for ELEMENT in y[0]:
        if ELEMENT in coordinate[2:]:
            y_cor = y[0].find(ELEMENT)

            break

    return x_cor, y_cor, direction_ships


def opponent():
    global opponent_grid
    opponent_grid = []

    for i in range(15):
        opponent_grid.append([])
        for j in range(15):
            ELEMENT = " O "
            if i > 10:
                ELEMENT = " X "
            opponent_grid[i].append(ELEMENT)

    x = ["ABCDEFGHIJ"]
    y = ["1234567890"]

    occupied = False
    global opponent_positions
    opponent_positions = {}
    ship_coordinates = {"Battleship": [1, 4],
                        "Cruiser": [2, 3],
                        "Destroyer": [3, 2],
                        "Submarine": [4, 1]}

    keys: str
    for keys in ship_coordinates:
        for i in range(ship_coordinates[keys][0]):
            direction = random.choice(["v", "h"])
            x_choice = random.choice(
                ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
            y_choice = random.choice(
                ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])

            coordinate = direction + x_choice + y_choice
            x_cor, y_cor, direction = input_processor(coordinate)

            direction_valid = direction_validity(
                ship_coordinates[keys][1], x_cor, y_cor, direction)

            while direction_valid == False:
                direction = random.choice(["v", "h"])
                x_choice = random.choice(
                    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
                y_choice = random.choice(
                    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

                coordinate = direction + x_choice + y_choice
                x_cor, y_cor, direction = input_processor(coordinate)

                direction_valid = direction_validity(
                    ship_coordinates[keys][1], x_cor, y_cor, direction)

            occupied = opponent_occupied(
                ship_coordinates[keys][1], x_cor, y_cor, direction)

            while occupied:
                direction = random.choice(["v", "h"])
                x_choice = random.choice(
                    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
                y_choice = random.choice(
                    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

                coordinate = direction + x_choice + y_choice
                x_cor, y_cor, direction = input_processor(coordinate)

                occupied = opponent_occupied(
                    ship_coordinates[keys][1], x_cor, y_cor, direction)

    # print(opponent_positions)
    return opponent_grid


grid = []

global player_positions
player_positions = {}

for i in range(15):
    grid.append([])
    for j in range(15):
        element = " O "
        if i > 10:
            element = " X "
        grid[i].append(element)

x = ["ABCDEFGHIJ"]
y = ["1234567890"]

occupied = False

ship_coordinates = {"Battleship": [1, 4],
                    "Cruiser": [1, 3],
                    "Destroyer": [1, 2],
                    "Submarine": [1, 1]}

for keys in ship_coordinates:
    for i in range(ship_coordinates[keys][0]):
        coordinate = input(f"Please enter the coordinates for {keys}: ")
        while check(coordinate) == False:
            coordinate = input(f"Please enter the coordinates for {keys}: ")
        x_cor, y_cor, direction = input_processor(coordinate)
        direction_valid = direction_validity(
            ship_coordinates[keys][1], x_cor, y_cor, direction)

        while direction_valid == False:
            while check(coordinate) == False:
                coordinate = input(
                    f"Please enter the coordinates for {keys}: ")
            x_cor, y_cor, direction = input_processor(coordinate)
            direction_valid = direction_validity(
                ship_coordinates[keys][1], x_cor, y_cor, direction)

        occupied = is_occupied(
            ship_coordinates[keys][1], x_cor, y_cor, direction)
        while occupied:
            while check(coordinate) == False:
                coordinate = input(
                    f"Please enter the coordinates for {keys}: ")
            x_cor, y_cor, direction = input_processor(coordinate)
            occupied = is_occupied(
                ship_coordinates[keys][1], x_cor, y_cor, direction)

        player_positions[coordinate] = []
        for j in range(ship_coordinates[keys][1]):
            if direction == "v":
                grid[y_cor + j][x_cor] = " X "
                player_positions[coordinate].append([y_cor + j, x_cor])

            elif direction == "h":
                grid[y_cor][x_cor + j] = " X "
                player_positions[coordinate].append([y_cor, x_cor + j])

        viewer(grid)
        print("Player Positions:", player_positions)

print()
print("EXCELLENT! YOU'RE READY TO ATTACK!")
# print("OPPONENT GRID")
opponent_grid = opponent()

# viewer(opponent_grid)

player_score = 0
opp_score = 0

win = False

round_num = 0

while not win:
    guess = input("Please enter a shooting coordinate_ships: ")
    while guess_checker(guess) == False:
        guess = input("Please enter a shooting coordinate_ships: ")
    first = x[0].find(guess[0].upper())
    second = y[0].find(guess[1])

    for keys in opponent_positions:
        for i in range(len(opponent_positions[keys])):
            if [second, first] == opponent_positions[keys][i]:
                opponent_positions[keys] = []
                player_score += 1
                print(
                    f"CONGRATS, BULL'S EYE!\nYour Score: {player_score}\nOpponent's Score: {opp_score}")
                break

    if player_score == 10:
        print("CONGRATS YOU DESTROYED THE ENEMY!")
        win = True

    x_choice = random.choice(
        ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
    y_choice = random.choice(
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    opp_guess = x_choice + y_choice
    first = x[0].find(opp_guess[0].upper())
    second = y[0].find(opp_guess[1])
    print("Opponent Shot:", opp_guess)
    for keys in player_positions:
        for i in range(len(player_positions[keys])):
            if [second, first] == player_positions[keys][i]:
                player_positions[keys] = []
                opp_score += 1
                print(
                    f"Oh no! Your ship is down!\nYour Score: {player_score}\nOpponent's Score: {opp_score}")
                break
            break
    if opp_score == 4:
        print("OOPS! YOU LOST!")
        win = True
    round_num += 1
    print(
        f"---------------\nROUND {round_num} SCORE\nYour Score: {player_score}\nOpponent's Score: {opp_score}\n---------------")

print(f"Your Score: {player_score}\nOpponent's Score: {opp_score}")

