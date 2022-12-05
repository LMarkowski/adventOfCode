import numpy as np


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def print_matrix(matrix):
    for line in matrix:
        print(line)
    print()


def main():
    data = read_file("data.txt")
    ship = []
    instructions = []

    split = 0
    for line in data:
        if line[1] == "1":
            break
        split += 1

    nb_of_cols = int((data[split].split())[-1])  # nb of containers stacks in the ship

    ship = data[:split]  # extract ship layout from data
    ship_matrix = []
    for line in ship:  # extract containers IDs from the ship data
        tmp = []
        for i in range(nb_of_cols):
            try:
                tmp.append(line[1 + (i) * 4])
            except:
                tmp.append(" ")
        ship_matrix.append(tmp)

    print("Initial layout of the ship:")
    print_matrix(ship_matrix)

    # transpose the matrix so each container stack becomes a row in the matrix
    ship_matrix = np.fliplr(np.transpose(ship_matrix)).tolist()
    for row in ship_matrix:
        row[:] = [value for value in row if value != " "]  # remove empty values

    print("Transposed and cleaned up for easier manipulation:")
    print_matrix(ship_matrix)

    instructions = data[-len(data) + split + 2 :]  # extract instructions from data
    instructions = [line.split() for line in instructions]
    for line in instructions:
        nb = int(line[1])  # nb of containers to be moved
        move_from = int(line[3]) - 1  # index of a stack to be moved from
        move_to = int(line[5]) - 1  # index of a stack to be moved to

        moving = []  # list of containers being moved

        # Moving containers one by one:
        # for i in range(nb):
        #     moving.append(ship_matrix[move_from].pop())

        # Moving containers by full stacks
        moving.extend(ship_matrix[move_from][-nb:])
        del ship_matrix[move_from][len(ship_matrix[move_from]) - nb :]

        ship_matrix[move_to].extend(moving)

    print("Final layout of the ship:")
    print_matrix(ship_matrix)

    print("Puzzle answer (top containers from each stack):")
    for row in ship_matrix:
        print(row[-1], end="")
    print()


if __name__ == "__main__":
    main()
