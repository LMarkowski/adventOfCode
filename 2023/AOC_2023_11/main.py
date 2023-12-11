import time

debug = 0  # 1 for testing | 0 for the final run


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def transpose(data):
    tmp = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    result = []
    for list in tmp:
        result += ["".join(list)]
    return result


def main():
    start_time = time.time()
    data = read_file("test-data.txt") if debug else read_file("data.txt")

    empty_rows = []
    empty_columns = []

    for i in range(len(data)):
        if "#" not in data[i]:
            empty_rows.append(i)
    data = transpose(data)
    for i in range(len(data)):
        if "#" not in data[i]:
            empty_columns.append(i)
    data = transpose(data)

    if debug:
        print(f"Empty rows: {empty_rows}")
        print(f"Empty columns: {empty_columns}")

    galaxies = []
    expansion = 1000000

    additional_rows = 0
    for i in range(len(data)):
        additional_columns = 0
        if i in empty_rows:
            additional_rows += 1
        for j in range(len(data[i])):
            if j in empty_columns:
                additional_columns += 1
            if data[i][j] == "#":
                new_i = i + additional_rows * (expansion - 1)
                new_j = j + additional_columns * (expansion - 1)
                if debug:
                    print(f"Galaxy: {len(galaxies) + 1}")
                    print(f"Additional rows: {additional_rows}")
                    print(f"Additional columns: {additional_columns}")
                    print(f"Original coordinates: {i}, {j}")
                    print(f"Expanded coordinates: {new_i}, {new_j}")
                galaxies.append((new_i, new_j))

    if debug:
        for i in range(len(galaxies)):
            print(f"{i+1}: {galaxies[i]}")

    pairs = []
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            pairs.append((galaxies[i], galaxies[j]))

    part_1 = 0

    for pair in pairs:
        manhattan_distance = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
        if debug:
            print(f"{galaxies.index(pair[0])+1}-{galaxies.index(pair[1])+1}: {manhattan_distance}")
        part_1 += manhattan_distance

    print(f"Galaxies: {len(galaxies)}")
    print(f"Pairs: {len(pairs)}")
    print(f"Sum of shortest paths: {part_1}")

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
