def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def draw_line(line):
    points = []
    start = line.pop()
    while line:
        next = line.pop()
        x0 = int(start[0])
        y0 = int(start[1])
        x1 = int(next[0])
        y1 = int(next[1])

        if x0 == x1:
            the_range = range(y0, y1 + 1) if y1 > y0 else range(y1, y0 + 1)
            for i in the_range:
                points.append((x0, i))

        if y0 == y1:
            the_range = range(x0, x1 + 1) if x0 < x1 else range(x1, x0 + 1)
            for i in the_range:
                points.append((i, y0))
        start = next

    return points


def print_on_grid(list, min_x, max_x, min_y, max_y):
    for x in range(min_y, max_y + 1):
        for y in range(min_x, max_x + 1):
            if x == 0 and y == 500:
                print("+", end="")
            elif (y, x) in list:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def main():
    debug = 0  # 1 for testing | 0 for the final run
    data = read_file("test-data.txt") if debug else read_file("data.txt")
    data_split = [[t.split(",") for t in line.split(" -> ")] for line in data]

    for line in data_split:
        print(line)

    lines = []
    for line in data_split:
        lines.append(draw_line(line))

    print()

    walls = [point for line in lines for point in line]

    max_x = max([t[0] for t in walls])
    min_x = min([t[0] for t in walls])
    max_y = max([t[1] for t in walls])
    min_y = 0  # source of sand is above the walls

    print_on_grid(walls, min_x, max_x, min_y, max_y)

    count = 0

    while True:
        count += 1
        new_grain = (500, 0)
        while True:
            next = (new_grain[0], new_grain[1] + 1)
            next_left = (new_grain[0] - 1, new_grain[1] + 1)
            next_right = (new_grain[0] + 1, new_grain[1] + 1)

            if next[1] == max_y + 2:
                walls.append(new_grain)
                break

            if next not in walls:
                new_grain = next
            elif next_left not in walls:
                new_grain = next_left
            elif next_right not in walls:
                new_grain = next_right
            else:
                walls.append(new_grain)
                break

            # part one
            # if new_grain[1] > max_y:
            #     break

        # part one
        # if new_grain[1] > max_y:
        #     break

        print(count)
        if (500, 0) in walls:
            break

    max_x = max([t[0] for t in walls])
    min_x = min([t[0] for t in walls])
    max_y = max([t[1] for t in walls])
    min_y = 0  # source of sand is above the walls

    # print_on_grid(walls, min_x, max_x, min_y, max_y)
    # print("part one", count - 1)
    print("grains", count)


if __name__ == "__main__":
    main()
