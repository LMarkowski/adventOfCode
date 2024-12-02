def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def main():
    data = read_file("input.txt")

    list_1 = []
    list_2 = []

    for line in data:
        list_1.append(int(line.split("   ")[0]))
        list_2.append(int(line.split("   ")[1]))

    list_1.sort()
    list_2.sort()

    sum_1 = 0
    sum_2 = 0

    for i in range(len(list_1)):
        count = list_2.count(list_1[i])
        if count > 0:
            sum_2 += list_1[i] * count
        sum_1 += abs(list_1[i] - list_2[i])

    print(sum_1)
    print(sum_2)


if __name__ == "__main__":
    main()
