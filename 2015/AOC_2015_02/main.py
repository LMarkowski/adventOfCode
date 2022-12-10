def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def main():
    debug = 0  # 1 for testing | 0 for the final run
    data = read_file("test-data.txt") if debug else read_file("data.txt")
    data_split = [line.split("x") for line in data]

    part_one = 0
    part_two = 0

    for line in data_split:
        x = int(line[0])
        y = int(line[1])
        z = int(line[2])

        areas = [2 * x * y, 2 * x * z, 2 * y * z]
        areas.append(min(areas) // 2)
        part_one += sum(areas)

        sides = [x, y, z]
        sides.remove(max(sides))
        part_two += 2 * sum(sides) + x * y * z

    print(part_one)
    print(part_two)


if __name__ == "__main__":
    main()
