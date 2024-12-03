def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


import re


def main():
    data = read_file("input.txt")
    data_concat = "".join(data)
    pattern = r"mul\((\d+),(\d+)\)"
    sum = 0

    pattern_first = r"^(.*?)don't\(\)"
    pattern_between = r"do\(\)(.*?)don't\(\)"
    pattern_last = r"do\(\)(.*?)$"

    to_execute = []

    to_execute.append(re.findall(pattern_first, data_concat)[0])
    to_execute += re.findall(pattern_between, data_concat)
    if "don't()" not in re.findall(pattern_last, data_concat)[0]:
        to_execute.append(re.findall(pattern_last, data_concat)[0])

    for line in to_execute:
        matches = re.findall(pattern, line)
        for match in matches:
            sum += int(match[0]) * int(match[1])

    print(sum)


if __name__ == "__main__":
    main()
