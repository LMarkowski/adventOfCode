def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def look_for_xmas(data: list[str], i: int, j: int) -> int:
    print(f"Found X at: [{i}, {j}]")
    found = 0
    possible_directions = []
    # look down
    if i < len(data) - 3:
        possible_directions.append("d")
    if i > 2:
        possible_directions.append("u")
    if j < len(data[i]) - 3:
        possible_directions.append("r")
    if j > 2:
        possible_directions.append("l")

    if "d" in possible_directions:
        if data[i + 1][j] == "M" and data[i + 2][j] == "A" and data[i + 3][j] == "S":
            print("Found down")
            found += 1
    if "u" in possible_directions:
        if data[i - 1][j] == "M" and data[i - 2][j] == "A" and data[i - 3][j] == "S":
            print("Found up")
            found += 1
    if "r" in possible_directions:
        if data[i][j + 1] == "M" and data[i][j + 2] == "A" and data[i][j + 3] == "S":
            print("Found right")
            found += 1
    if "l" in possible_directions:
        if data[i][j - 1] == "M" and data[i][j - 2] == "A" and data[i][j - 3] == "S":
            print("Found left")
            found += 1
    if "d" in possible_directions and "r" in possible_directions:
        if data[i + 1][j + 1] == "M" and data[i + 2][j + 2] == "A" and data[i + 3][j + 3] == "S":
            print("Found down right")
            found += 1
    if "d" in possible_directions and "l" in possible_directions:
        if data[i + 1][j - 1] == "M" and data[i + 2][j - 2] == "A" and data[i + 3][j - 3] == "S":
            print("Found down left")
            found += 1
    if "u" in possible_directions and "r" in possible_directions:
        if data[i - 1][j + 1] == "M" and data[i - 2][j + 2] == "A" and data[i - 3][j + 3] == "S":
            print("Found up right")
            found += 1
    if "u" in possible_directions and "l" in possible_directions:
        if data[i - 1][j - 1] == "M" and data[i - 2][j - 2] == "A" and data[i - 3][j - 3] == "S":
            print("Found up left")
            found += 1

    return found


def look_for_x_mas(data: list[str], i: int, j: int) -> int:
    found = 0
    if i == 0 or i == len(data) - 1 or j == 0 or j == len(data[i]) - 1:
        return 0

    if (
        data[i - 1][j - 1] == "M"
        and data[i - 1][j + 1] == "S"
        and data[i + 1][j - 1] == "M"
        and data[i + 1][j + 1] == "S"
    ):
        print(f"Found X-MAS at: [{i}, {j}]")
        found += 1

    if (
        data[i - 1][j - 1] == "M"
        and data[i - 1][j + 1] == "M"
        and data[i + 1][j - 1] == "S"
        and data[i + 1][j + 1] == "S"
    ):
        print(f"Found X-MAS at: [{i}, {j}]")
        found += 1

    if (
        data[i - 1][j - 1] == "S"
        and data[i - 1][j + 1] == "S"
        and data[i + 1][j - 1] == "M"
        and data[i + 1][j + 1] == "M"
    ):
        print(f"Found X-MAS at: [{i}, {j}]")
        found += 1

    if (
        data[i - 1][j - 1] == "S"
        and data[i - 1][j + 1] == "M"
        and data[i + 1][j - 1] == "S"
        and data[i + 1][j + 1] == "M"
    ):
        print(f"Found X-MAS at: [{i}, {j}]")
        found += 1

    return found


def main():
    data = read_file("input.txt")

    # data = [
    #     "MMMSXXMASM",
    #     "MSAMXMSMSA",
    #     "AMXSXMAAMM",
    #     "MSAMASMSMX",
    #     "XMASAMXAMM",
    #     "XXAMMXXAMA",
    #     "SMSMSASXSS",
    #     "SAXAMASAAA",
    #     "MAMMMXMMMM",
    #     "MXMXAXMASX",
    # ]

    sum_1 = 0
    sum_2 = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "X":
                sum_1 += look_for_xmas(data, i, j)
                print(f"Current sum: {sum_1}")
                print()
            if data[i][j] == "A":
                sum_2 += look_for_x_mas(data, i, j)

    print(sum_1)
    print(sum_2)


if __name__ == "__main__":
    main()
