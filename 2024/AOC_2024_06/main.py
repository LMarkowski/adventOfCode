def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


debug = False
directions = ["u", "r", "d", "l"]


def run(current_pos, current_dir, data_arg):
    loop = False
    been = []
    directions = ["u", "r", "d", "l"]

    while current_pos[0] in range(len(data_arg[0])) and current_pos[1] in range(len(data_arg)):
        if debug:
            print(f"Current pos: {current_pos}, {current_dir}")

        if current_pos[0] == 0 and current_dir == "l":
            break
        if current_pos[0] == len(data_arg[0]) - 1 and current_dir == "r":
            break
        if current_pos[1] == 0 and current_dir == "u":
            break
        if current_pos[1] == len(data_arg) - 1 and current_dir == "d":
            break

        if current_dir == "u":
            if data_arg[current_pos[1] - 1][current_pos[0]] in "#O":
                current_dir = directions[(directions.index(current_dir) + 1) % 4]
            else:
                current_pos[1] -= 1
        elif current_dir == "r":
            if data_arg[current_pos[1]][current_pos[0] + 1] in "#O":
                current_dir = directions[(directions.index(current_dir) + 1) % 4]
            else:
                current_pos[0] += 1
        elif current_dir == "d":
            if data_arg[current_pos[1] + 1][current_pos[0]] in "#O":
                current_dir = directions[(directions.index(current_dir) + 1) % 4]
            else:
                current_pos[1] += 1
        elif current_dir == "l":
            if data_arg[current_pos[1]][current_pos[0] - 1] in "#O":
                current_dir = directions[(directions.index(current_dir) + 1) % 4]
            else:
                current_pos[0] -= 1
        if (tuple(current_pos), current_dir) in been:
            if debug:
                print(f"Already been at: {current_pos}, {current_dir}")
            loop = True
            break
        been.append((tuple(current_pos), current_dir))
        line_list = list(data_arg[current_pos[1]])
        line_list[current_pos[0]] = "X"
        data_arg[current_pos[1]] = "".join(line_list)

    if loop and debug:
        print_data(data_arg)
    return loop, been


def print_data(data):
    for line in data:
        print(line)


def main():
    data = read_file("input.txt")
    for line in data:
        if "^" in line:
            x = line.index("^")
            y = data.index(line)

    sum = 0
    data_copy = data.copy()
    loop, initial_been = run([x, y], directions[0], data_copy)

    been_positions = [p[0] for p in initial_been]
    been_positions = list(set(been_positions))
    print(f"Part 1: {len(been_positions)}")

    count = 0
    for pos in been_positions:
        count += 1
        print() if debug else None
        i = pos[1]
        j = pos[0]
        if data[i][j] == "#":
            continue

        new_data = data.copy()
        line_list = list(new_data[i])
        line_list[j] = "O"
        new_data[i] = "".join(line_list)

        initial_pos = [x, y]
        if debug:
            print(f"Checking {count}/{len(been_positions)}")
        if run(initial_pos, directions[0], new_data)[0]:
            sum += 1
            print(f"Loop found at: [{j}, {i}]") if debug else None
        else:
            print(f"No loop found.") if debug else None

    print(f"Part 2: {sum}")


if __name__ == "__main__":
    main()
