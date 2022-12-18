import time


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def get_surface_area(point, list):
    result = 0

    if (point[0] - 1, point[1], point[2]) not in list:
        result += 1
    if (point[0] - 1, point[1], point[2]) not in list:
        result += 1
    if (point[0], point[1] - 1, point[2]) not in list:
        result += 1
    if (point[0], point[1] + 1, point[2]) not in list:
        result += 1
    if (point[0], point[1], point[2] - 1) not in list:
        result += 1
    if (point[0], point[1], point[2] + 1) not in list:
        result += 1

    return result


def bfs(start, bbox, walls, goal):
    queue = [start]
    explored_coords = [(queue[0][0], queue[0][1], queue[0][2])]

    # Breadth-first search alorithm
    while queue:
        current = queue.pop(0)
        if current == goal:
            return True
        for next in possible_paths(current, bbox, walls, goal):
            if (next[0], next[1], next[2]) not in explored_coords:
                explored_coords.append((next[0], next[1], next[2]))
                queue.append(next)
    return False


def bfs_explored_paths(start, bbox, walls, goal):
    queue = [start]
    explored_coords = [(queue[0][0], queue[0][1], queue[0][2])]

    while queue:
        current = queue.pop(0)
        if current == goal:
            return explored_coords
        for next in possible_paths(current, bbox, walls, goal):
            if (next[0], next[1], next[2]) not in explored_coords:
                explored_coords.append((next[0], next[1], next[2]))
                queue.append(next)
    return explored_coords


def possible_paths(point, bbox, walls, goal):
    paths = []
    if point[0] > bbox["min_x"]:
        paths.append(
            (
                point[0] - 1,
                point[1],
                point[2],
            )
        )
    if point[0] < bbox["max_x"]:
        paths.append(
            (
                point[0] + 1,
                point[1],
                point[2],
            )
        )
    if point[1] > bbox["min_y"]:
        paths.append(
            (
                point[0],
                point[1] - 1,
                point[2],
            )
        )
    if point[1] < bbox["max_y"]:
        paths.append(
            (
                point[0],
                point[1] + 1,
                point[2],
            )
        )
    if point[2] > bbox["min_z"]:
        paths.append(
            (
                point[0],
                point[1],
                point[2] - 1,
            )
        )
    if point[2] < bbox["max_z"]:
        paths.append(
            (
                point[0],
                point[1],
                point[2] + 1,
            )
        )

    if goal in paths:
        return [goal]
    else:
        return [x for x in paths if not x in walls]


# main task finishes in 8.4s
def main():
    start_time = time.time()

    debug = 1  # 1 for testing | 0 for the final run
    data = read_file("test-data.txt") if debug else read_file("data.txt")
    all_points = [tuple([int(x) for x in line.split(",")]) for line in data]

    part_one_total = 0
    for point in all_points:
        part_one_total += get_surface_area(point, all_points)
    print("Part one:")
    print(part_one_total)

    bbox = {
        "min_x": min([t[0] for t in all_points]) - 2,
        "max_x": max([t[0] for t in all_points]) + 2,
        "min_y": min([t[1] for t in all_points]) - 2,
        "max_y": max([t[1] for t in all_points]) + 2,
        "min_z": min([t[2] for t in all_points]) - 2,
        "max_z": max([t[2] for t in all_points]) + 2,
    }

    start = (bbox["min_x"] + 1, bbox["min_y"] + 1, bbox["min_z"] + 1)

    # running bfs for an unobtainable goal so it return all possible fields around the rock
    surroundings = bfs_explored_paths(start, bbox, all_points, (1000, 1000, 1000))

    # filling the gaps inside the rock
    for x in range(bbox["min_x"], bbox["max_x"] + 1):
        for y in range(bbox["min_y"], bbox["max_y"] + 1):
            for z in range(bbox["min_z"], bbox["max_z"] + 1):
                if (x, y, z) not in surroundings and (x, y, z) not in all_points:
                    all_points.append((x, y, z))

    # same approach as part one, but the rock is now solid
    part_two_total = 0
    for point in all_points:
        part_two_total += get_surface_area(point, all_points)
    print("Part two:")
    print(part_two_total)

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
