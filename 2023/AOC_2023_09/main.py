import time

debug = 0  # 1 for testing | 0 for the final run


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def main():
    start_time = time.time()
    data = read_file("test-data.txt") if debug else read_file("data.txt")

    data = [[int(i) for i in line.split()] for line in data]
    differences = []

    for line in data:
        current = line
        tmp = []
        tmp_diff = []
        steps = 0
        while True:
            steps += 1
            for i in range(len(current) - 1):
                tmp.append(current[i + 1] - current[i])
            tmp_diff.append(tmp)
            if sum(tmp) == 0:
                differences.append(tmp_diff)
                break
            current = tmp
            tmp = []

    part_1 = 0
    for i in range(len(data)):
        next_number = data[i][-1] + [sum(l[-1] for l in differences[i])][0]
        part_1 += next_number

    print(f"Part 1: {part_1}")

    part_2 = 0
    for i in range(len(data)):
        tmp = 0
        for j in range(len(differences[i])):
            tmp = differences[i][-1 - j][0] - tmp
        part_2 += data[i][0] - tmp

    print(f"Part 2: {part_2}")

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
