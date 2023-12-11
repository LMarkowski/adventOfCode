import time

debug = 0  # 1 for testing | 0 for the final run


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def is_point_in_path(x: int, y: int, poly) -> bool:
    """Determine if the point is on the path, corner, or boundary of the polygon

    Args:
      x -- The x coordinates of point.
      y -- The y coordinates of point.
      poly -- a list of tuples [(x, y), (x, y), ...]

    Returns:
      True if the point is in the path or is a corner or on the boundary"""
    num = len(poly)
    j = num - 1
    c = False
    for i in range(num):
        if (x == poly[i][0]) and (y == poly[i][1]):
            # point is a corner
            return False
        if (poly[i][1] > y) != (poly[j][1] > y):
            slope = (x - poly[i][0]) * (poly[j][1] - poly[i][1]) - (poly[j][0] - poly[i][0]) * (
                y - poly[i][1]
            )
            if slope == 0:
                # point is on boundary
                return False
            if (slope < 0) != (poly[j][1] < poly[i][1]):
                c = not c
        j = i
    return c


def main():
    start_time = time.time()
    map = read_file("test-data.txt") if debug else read_file("data.txt")

    loop = []

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                loop.append((i, j))
                x = i
                y = j

    right = "J-7"
    left = "F-L"
    up = "F|7"
    down = "J|L"

    if map[x + 1][y] in down:
        loop.append((x + 1, y))
    elif map[x][y + 1] in right:
        loop.append((x, y + 1))
    elif map[x - 1][y] in up:
        loop.append((x - 1, y))
    elif map[x - 1][y] in left:
        loop.append((x - 1, y))

    while True:
        current = loop[-1]
        x = current[0]
        y = current[1]
        added = False
        if map[x][y] == "L":
            if (x - 1, y) not in loop:
                loop.append((x - 1, y))
                added = True
            if (x, y + 1) not in loop:
                loop.append((x, y + 1))
                added = True
        elif map[x][y] == "J":
            if (x, y - 1) not in loop:
                loop.append((x, y - 1))
                added = True
            if (x - 1, y) not in loop:
                loop.append((x - 1, y))
                added = True
        elif map[x][y] == "F":
            if (x + 1, y) not in loop:
                loop.append((x + 1, y))
                added = True
            if (x, y + 1) not in loop:
                loop.append((x, y + 1))
                added = True
        elif map[x][y] == "7":
            if (x, y - 1) not in loop:
                loop.append((x, y - 1))
                added = True
            if (x + 1, y) not in loop:
                loop.append((x + 1, y))
                added = True
        elif map[x][y] == "|":
            if (x + 1, y) not in loop:
                loop.append((x + 1, y))
                added = True
            if (x - 1, y) not in loop:
                loop.append((x - 1, y))
                added = True
        elif map[x][y] == "-":
            if (x, y + 1) not in loop:
                loop.append((x, y + 1))
                added = True
            if (x, y - 1) not in loop:
                loop.append((x, y - 1))
                added = True
        if not added:
            break

    print("Part 1:", int(len(loop) / 2))

    part_2 = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if is_point_in_path(i, j, loop):
                part_2 += 1

    print(f"Part 2: {part_2}")

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
