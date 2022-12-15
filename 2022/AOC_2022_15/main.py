import re
import time


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def print_on_grid(sensors, beacons, not_possibe, min_x, max_x, min_y, max_y):
    for x in range(min_y, max_y + 1):
        for y in range(min_x, max_x + 1):
            if (y, x) in beacons:
                print("B", end="")
            elif (y, x) in sensors:
                print("S", end="")
            elif (y, x) in not_possibe:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def manhattan(point, other):
    return abs(point[0] - other[0]) + abs(point[1] - other[1])


def remove_dupes(mylist):
    newlist = [mylist[0]]
    for e in mylist:
        if e not in newlist:
            newlist.append(e)
    return newlist


def main():
    start_time = time.time()

    debug = 1  # 1 for testing | 0 for the final run
    data = read_file("test-data.txt") if debug else read_file("data.txt")
    sensors = []
    beacons = []
    for line in data:
        x = re.findall("x=-?\d+", line)
        y = re.findall("y=-?\d+", line)

        sensors.append((int(x[0][2:]), int(y[0][2:])))
        beacons.append((int(x[1][2:]), int(y[1][2:])))

    print("Parsed data.")

    all = list(sensors)
    all.extend(beacons)

    max_x = max([t[0] for t in all])
    min_x = min([t[0] for t in all])
    max_y = max([t[1] for t in all])
    min_y = min([t[1] for t in all])

    distances = []

    for sensor, beacon in zip(sensors, beacons):
        distances.append(manhattan(sensor, beacon))

    print("Calculated all distances.")

    important_y = 10 if debug else 2000000
    result = []
    max_distance = max(distances)

    to_check = max_x + max_distance + 1 - (min_x - max_distance)
    count = 0

    for x in range(min_x - max_distance, max_x + max_distance + 1):
        for sensor, distance in zip(sensors, distances):
            if manhattan((x, important_y), sensor) <= distance:
                if (x, important_y) not in sensors and (x, important_y) not in beacons:
                    result.append((x, important_y))

    print("Part one:")
    print(len(set(result)))

    points_to_check = []

    p2_min = 0
    p2_max = 20 if debug else 4000000

    count = 0

    for sensor, distance in zip(sensors, distances):
        print(count)
        x = sensor[0] + distance + 1
        y = sensor[1]
        while x != sensor[0]:
            if x >= 0 and x <= p2_max and y >= 0 and y <= p2_max:
                points_to_check.append((x, y))
            x -= 1
            y += 1

        while y != sensor[1]:
            if x >= 0 and x <= p2_max and y >= 0 and y <= p2_max:
                points_to_check.append((x, y))
            x -= 1
            y -= 1

        while x != sensor[0]:
            if x >= 0 and x <= p2_max and y >= 0 and y <= p2_max:
                points_to_check.append((x, y))
            x += 1
            y -= 1

        while y != sensor[1]:
            if x >= 0 and x <= p2_max and y >= 0 and y <= p2_max:
                points_to_check.append((x, y))
            x += 1
            y += 1

        count += 1

    print("got all point")

    print(len(points_to_check))

    of = len(points_to_check)
    count = 0

    for point in points_to_check:
        print(count, "of", of)
        not_beacon = True
        for sensor, distance in zip(sensors, distances):
            if manhattan(point, sensor) <= distance:
                not_beacon = False
                break
        if not_beacon:
            result = point
            break
        count += 1

    print("Part two:")
    print(4000000 * result[0] + result[1])

    # if debug:
    #     print_on_grid(sensors, beacons, points_to_check, 0, 20, 0, 20)

    print(f"Finished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
