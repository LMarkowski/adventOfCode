def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def is_containing(pair, other):
    if pair[0] <= other[0] and pair[1] >= other[1]:
        return True
    else:
        return False


def is_overlapping(pair, other):
    if pair[1] >= other[0] and pair[0] <= other[1]:
        return True
    else:
        return False


def main():
    data = read_file("data.txt")
    data_split = [line.split(",") for line in data]
    numbers = []

    for pair in data_split:
        elf_1 = [int(txt) for txt in pair[0].split("-")]
        elf_2 = [int(txt) for txt in pair[1].split("-")]
        numbers.append([elf_1, elf_2])

    fully_contained = 0
    for pair in numbers:
        if is_containing(pair[0], pair[1]) or is_containing(pair[1], pair[0]):
            fully_contained += 1

    overlapping = 0
    for pair in numbers:
        if is_overlapping(pair[0], pair[1]) or is_overlapping(pair[1], pair[0]):
            overlapping += 1

    print(fully_contained)
    print(overlapping)


if __name__ == "__main__":
    main()
