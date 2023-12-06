import time
from math import floor, ceil

debug = 0  # 1 for testing | 0 for the final run


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def distance(time, time_charging):
    dist = -(time_charging**2) + time_charging * time
    return dist


def time_charging_to_beat(time, distance):
    a = -1
    b = time
    c = -distance
    delta = b**2 - 4 * a * c
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)

    return (x1, x2)


def main():
    start_time = time.time()
    data = read_file("test-data.txt") if debug else read_file("data.txt")

    times = data[0].split()[1:]
    dists = data[1].split()[1:]

    times = [int(i) for i in times]
    dists = [int(i) for i in dists]

    print(times)
    print(dists)

    score = 1
    for t, d in zip(times, dists):
        roots = time_charging_to_beat(t, d)
        if roots[0] == ceil(roots[0]):
            lowest_time = roots[0] + 1
        else:
            lowest_time = ceil(roots[0])
        if roots[1] == ceil(roots[1]):
            highest_time = roots[1] - 1
        else:
            highest_time = floor(roots[1])

        possible_times = int(highest_time - lowest_time + 1)

        print(possible_times)
        score *= possible_times

    print(f"Answer: {score}")

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
