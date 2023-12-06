import time

debug = 0  # 1 for testing | 0 for the final run


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def boundary_range(number, coords, data):
    range_x = (coords[0] - 1, coords[0] + len(str(number)) + 1)
    range_y = (coords[1] - 1, coords[1] + 2)
    if range_x[0] < 0:
        range_x = (0, range_x[1])
    if range_y[0] < 0:
        range_y = (0, range_y[1])
    if range_x[1] > len(data[0]):
        range_x = (range_x[0], len(data[0]))
    if range_y[1] > len(data):
        range_y = (range_y[0], len(data))

    return range_x, range_y


def find_gears_in_range(range_x, range_y, data):
    gears = []
    for i in range(range_y[0], range_y[1]):
        for j in range(range_x[0], range_x[1]):
            if data[i][j] == "*":
                gears.append((i, j))
    return gears


def find_numbers(data):
    numbers = []
    reading = False
    tmp_nb = ""
    tmp_coords = ()

    for y in range(len(data)):
        if reading:
            reading = False
            numbers.append((int(tmp_nb), tmp_coords))
            tmp_nb = ""
            tmp_coords = ()

        for x in range(len(data[y])):
            if data[y][x] in "0123456789":
                if not reading:
                    reading = True
                    tmp_coords = (x, y)
                tmp_nb += data[y][x]
            else:
                if reading:
                    reading = False
                    numbers.append((int(tmp_nb), tmp_coords))
                    tmp_nb = ""
                    tmp_coords = ()

    return numbers


def is_valid_number(number, coords, data):
    range_x, range_y = boundary_range(number, coords, data)

    if debug:
        print(f"Checking number {number}")
        print(f"Range x: {range_x}")
        print(f"Range y: {range_y}")

    for i in range(range_y[0], range_y[1]):
        for j in range(range_x[0], range_x[1]):
            if debug:
                print(f"({i},{j} - ", end=" ")
                print(f"{data[i][j]})")
            if data[i][j] not in ".0123456789":
                if debug:
                    print("breaking")
                return False
    return True


def main():
    start_time = time.time()
    data = read_file("test-data.txt") if debug else read_file("data.txt")

    if debug:
        for line in data:
            print(line)

    numbers = find_numbers(data)  # list of tuples (number, starting_coords)

    if debug:
        for line in numbers:
            print(line)

    # Part 1
    sum = 0
    for number in numbers:
        value = number[0]
        coords = number[1]
        range_x, range_y = boundary_range(value, coords, data)

        if is_valid_number(value, coords, data):
            sum += value

    print(f"Part 1: {sum}")

    # Part 2
    adjacent_gears = []  # list matching numbers with their adjacent gears by index
    sum = 0
    for number in numbers:
        value = number[0]
        coords = number[1]
        range_x, range_y = boundary_range(value, coords, data)

        if debug:
            print(f"Checking number {value}")
            print(f"Range x: {range_x}")
            print(f"Range y: {range_y}")

        adjacent_gears.append(find_gears_in_range(range_x, range_y, data))

    for i in range(len(adjacent_gears)):
        for j in range(i + 1, len(adjacent_gears)):
            if len(set(adjacent_gears[i]) & set(adjacent_gears[j])) > 0:
                sum += numbers[i][0] * numbers[j][0]

    print(f"Part 2: {sum}")

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
