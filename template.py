def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def main():
    debug = False
    data = read_file("test-data.txt") if debug else read_file("data.txt")


if __name__ == "__main__":
    main()
