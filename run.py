# -*- coding: utf-8 -*-
import random


def guess_checker(guess):
    if (guess[0].upper() in x[0]) and (guess[1] in y[0]):
        return True
    else:
        print("*PLEASE ENTER A VALID COORDINATE!")
        return False


def viewer(matrix):
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
    if direction == "v":
        if occupying_area <= 11 - y_cor:
            return True
        print(
 f"[Your coordinates are out of boundaries. Please enter a valid coordinate!] [coordinate states the upper most left coordinate of the ship.]")
        return False

    elif direction == "h":
        if occupying_area <= 11 - x_cor:
            return True
        return False


def isOccupied(occupying_area, x_cor, y_cor, direction):
    for i in range(1, occupying_area):

        if direction == "v":
            if grid[y_cor + i][x_cor] == " X ":
                print(
                    "There is already another ship intersecting with these coordinates!")
                return True
            else:
                continue

            return False
        elif direction == "h":
            if grid[y_cor][x_cor + i] == " X ":
                print(
                    "There is already another ship intersecting with these coordinates!")
                return True
            else:
                continue


def opponentOccupied(occupying_area, x_cor, y_cor, direction):
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


def check(coordinate):
    if ((len(coordinate) == 3) and (coordinate[0].lower() == "v" or coordinate[0].lower() == "h") and (
            coordinate[1].upper() in x[0]) and (coordinate[2] in y[0])):
        return True
    else:
        print("*PLEASE ENTER A VALID COORDINATE!")
        return False


def inputProcessor(coordinate):
    direction = coordinate[0].lower()

    for element in x[0]:

        if element in coordinate[1:2].upper():
            x_cor = x[0].find(element)

            break

    for element in y[0]:
        if element in coordinate[2:]:
            y_cor = y[0].find(element)

            break

    return x_cor, y_cor, direction


def opponent():
    global opponent_grid
    opponent_grid = []

    for i in range(15):
        opponent_grid.append([])
        for j in range(15):
            element = " O "
            if i > 10:
                element = " X "
            opponent_grid[i].append(element)

    x = ["ABCDEFGHIJ"]
    y = ["1234567890"]

    occupied = False
    global opponent_positions
    opponent_positions = {}

    ship_coordinates = {"Battleship": [1, 4],
                        "Cruiser": [2, 3],
                        "Destroyer": [3, 2],
                        "Submarine": [4, 1]}

    for keys in ship_coordinates:
        for i in range(ship_coordinates[keys][0]):
            direction = random.choice(["v", "h"])
            x_choice = random.choice(
                ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
            y_choice = random.choice(
                ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])

            coordinate = direction + x_choice + y_choice
            x_cor, y_cor, direction = inputProcessor(coordinate)

            directionValid = direction_validity(
                ship_coordinates[keys][1], x_cor, y_cor, direction)

            while directionValid == False:
                direction = random.choice(["v", "h"])
                x_choice = random.choice(
                    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
                y_choice = random.choice(
                    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

                coordinate = direction + x_choice + y_choice
                x_cor, y_cor, direction = inputProcessor(coordinate)

                directionValid = direction_validity(
                    ship_coordinates[keys][1], x_cor, y_cor, direction)

            occupied = opponentOccupied(
                ship_coordinates[keys][1], x_cor, y_cor, direction)

            while occupied:
                direction = random.choice(["v", "h"])
                x_choice = random.choice(
                    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
                y_choice = random.choice(
                    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

                coordinate = direction + x_choice + y_choice
                x_cor, y_cor, direction = inputProcessor(coordinate)

                occupied = opponentOccupied(
                    ship_coordinates[keys][1], x_cor, y_cor, direction)

            opponent_positions[coordinate] = []
            for j in range(ship_coordinates[keys][1]):
                if direction == "v":
                    opponent_grid[y_cor + j][x_cor] = " X "

                    opponent_positions[coordinate].append([y_cor + j, x_cor])

                elif direction == "h":
                    opponent_grid[y_cor][x_cor + j] = " X "

                    opponent_positions[coordinate].append([y_cor, x_cor + j])

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

        x_cor, y_cor, direction = inputProcessor(coordinate)

        directionValid = direction_validity(
            ship_coordinates[keys][1], x_cor, y_cor, direction)

        while directionValid == False:
            while check(coordinate) == False:
                coordinate = input(
                    f"Please enter the coordinates for {keys}: ")
            x_cor, y_cor, direction = inputProcessor(coordinate)
            directionValid = direction_validity(
                ship_coordinates[keys][1], x_cor, y_cor, direction)

        occupied = isOccupied(
            ship_coordinates[keys][1], x_cor, y_cor, direction)
        while occupied:
            while check(coordinate) == False:
                coordinate = input(
                    f"Please enter the coordinates for {keys}: ")
            x_cor, y_cor, direction = inputProcessor(coordinate)
            occupied = isOccupied(
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
    guess = input("Please enter a shooting coordinate: ")
    while guess_checker(guess) == False:
        guess = input("Please enter a shooting coordinate: ")
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
