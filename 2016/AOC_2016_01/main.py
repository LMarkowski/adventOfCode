def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


data = read_file("input.txt")
data = data[0].split(", ")

coords = [0, 0]
direction = 0
visited_locations = []


for instruction in data:
    turn = instruction[0]
    steps = int(instruction[1:])

    if turn == "R":
        direction += 1
    elif turn == "L":
        direction -= 1

    direction %= 4

    for _ in range(steps):
        if direction == 0:
            coords[1] += 1
        elif direction == 1:
            coords[0] += 1
        elif direction == 2:
            coords[1] -= 1
        elif direction == 3:
            coords[0] -= 1

        if coords in visited_locations:
            print(f"Part 2: {abs(coords[0]) + abs(coords[1])}")
            exit(0)

        visited_locations.append(coords.copy())
