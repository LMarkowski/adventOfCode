def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def split_list(list, sep):
    tmp = []
    result = []
    for entry in list:
        if entry == sep and len(tmp) != 0:
            result.append(tmp)
            tmp = []
        else:
            tmp.append(entry)
    return result


def get_top_scores(list, nb):
    if nb > len(list):
        return -1
    list.sort()
    return list[-nb:]


def main():
    data = read_file("data.txt")
    data_split = split_list(data, "")
    sums = [sum(map(int, elf)) for elf in data_split]
    print(max(sums))
    print()
    print(sum(get_top_scores(sums, 3)))


if __name__ == "__main__":
    main()
