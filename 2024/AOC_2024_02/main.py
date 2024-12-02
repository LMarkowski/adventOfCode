def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def check_list(data):
    increasing = data[0] >= data[1]
    for i in range(len(data) - 1):
        still_increasing = (data[i] >= data[i + 1]) == increasing
        safe = (abs(data[i + 1] - data[i]) >= 1) and (abs(data[i + 1] - data[i]) <= 3)

        if not still_increasing or not safe:
            return False

    return True


def main():
    data = read_file("input.txt")
    data_split = []
    for line in data:
        data_split.append([int(x) for x in line.split(" ")])

    sum = 0

    for i in range(len(data_split)):
        found = False
        print(f"Checking list {i}: {data_split[i]}")
        print(f"Initial check: {check_list(data_split[i])}")
        if check_list(data_split[i]):
            found = True
            sum += 1
            print(f"Valid full list {i}: {data_split[i]}")
            print(f"current sum: {sum}")
            print()
            continue

        for j in range(len(data_split[i])):
            new_list = data_split[i].copy()
            del new_list[j]
            print(f"Checking partial list {i}: {new_list}")

            if check_list(new_list):
                found = True
                print(f"Valid partial list {i}: {new_list}")
                sum += 1
                break

        print()

    print(sum)


if __name__ == "__main__":
    main()
