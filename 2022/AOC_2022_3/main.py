def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def make_alphabet():
    result = [0]
    # first element is set to 0
    # so indices of each letter
    # match their priority

    start = ord("a")
    for i in range(26):
        result.append(chr(start))
        start += 1

    start = ord("A")
    for i in range(26):
        result.append(chr(start))
        start += 1

    return result


def main():
    data = read_file("data.txt")
    priorities = make_alphabet()

    rucksacks_pockets = [
        [line[: len(line) // 2], line[len(line) // 2 :]] for line in data
    ]
    first_score = 0
    for rucksack in rucksacks_pockets:
        common_elements = list(set(rucksack[0]).intersection(rucksack[1]))
        first_score += priorities.index(common_elements[0])

    print(first_score)

    groups_of_three = [data[i : i + 3] for i in range(0, len(data), 3)]
    second_score = 0
    for group in groups_of_three:
        common_elements = list(
            set(group[0]).intersection(group[1]).intersection(group[2])
        )
        second_score += priorities.index(common_elements[0])

    print(second_score)


if __name__ == "__main__":
    main()
