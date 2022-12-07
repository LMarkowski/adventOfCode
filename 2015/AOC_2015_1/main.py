def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def main():
    filename = "data.txt"
    data = read_file(filename)[0]

    floor = 0
    count = 0
    stop_count = False

    for charachter in data:
        if not stop_count:
            count += 1

        if charachter == "(":
            floor += 1
        elif charachter == ")":
            floor -= 1

        if floor == -1:
            stop_count = True

    print("Part one:")
    print(f"Santa will end up on the {floor}(th) floor.")
    print("Part two:")
    print(f"Santa will first enter the basement after the {count}(th) instruction.")


if __name__ == "__main__":
    main()
