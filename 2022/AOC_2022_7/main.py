def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def go_up_one_directory(path):
    path = path.split("/")
    del path[-2]
    return "/".join(path)


def list_all_directories_above(path):
    result = [path]
    while path != "/":
        path = go_up_one_directory(path)
        result.append(path)
    return result


# Creates a dictionary with sizes of all directories
def make_directories_dict(log):
    result = {}
    current_path = ""

    for line in log:
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    current_path = "/"
                elif line[2] == "..":
                    current_path = go_up_one_directory(current_path)
                else:
                    current_path += f"{line[2]}/"
        elif line[0].isdigit():  # so if it's a file with a specified size
            for dir in list_all_directories_above(current_path):
                if dir in result:
                    result[dir] += int(line[0])
                else:
                    result[dir] = int(line[0])
    return result


def main():
    data = read_file("data.txt")
    data_split = [line.split() for line in data]

    # Dictionary with sizes of all directories
    directory_size_dict = make_directories_dict(data_split)

    # Part one
    sum = 0
    for key in directory_size_dict:
        if directory_size_dict[key] <= 100000:
            sum += directory_size_dict[key]

    print("Answer to part 1:\n", sum)
    print()

    # Part two
    total = 70000000
    needs = 30000000
    used = directory_size_dict["/"]
    avail = total - used
    to_free = needs - avail

    print("Total:        ", total)
    print("Used:         ", used)
    print("Needs:        ", needs)
    print("Available:    ", avail)
    print("Needs to free:", to_free)

    min = used
    for key in directory_size_dict:
        if directory_size_dict[key] >= to_free and directory_size_dict[key] < min:
            min = directory_size_dict[key]

    print()
    print("Answer to part 2:\n", min)
    print()


if __name__ == "__main__":
    main()
