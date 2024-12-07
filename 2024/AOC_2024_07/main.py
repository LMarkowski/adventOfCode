import itertools


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


debug = False


def find_combinations(operations, number):
    return ["".join(comb) for comb in itertools.product(operations, repeat=number)]


def check(combinations, numbers, result):
    for combination in combinations:
        current_result = numbers[0]
        for i in range(len(combination)):
            if combination[i] == "+":
                current_result += numbers[i + 1]
            elif combination[i] == "*":
                current_result *= numbers[i + 1]
            elif combination[i] == "|":
                current_result = int(str(current_result) + str(numbers[i + 1]))
        if current_result == result:
            return True
    return False


def print_data(data):
    for line in data:
        print(line)


def main():
    data = read_file("input.txt")

    instructions = []

    for line in data:
        result = int(line.split(":")[0])
        numbers = line.split(":")[1][1:].split(" ")
        numbers = [int(x) for x in numbers]
        instructions.append((result, numbers))

    operations_1 = "+*"
    operations_2 = "+*|"

    sum_1 = 0
    sum_2 = 0

    for instruction in instructions:
        result = instruction[0]
        numbers = instruction[1]
        combinations_1 = find_combinations(operations_1, len(numbers) - 1)
        combinations_2 = find_combinations(operations_2, len(numbers) - 1)
        possible_1 = False
        possible_2 = False

        for combination in combinations_1:
            if check([combination], numbers, result):
                possible_1 = True
                break
        for combination in combinations_2:
            if check([combination], numbers, result):
                possible_2 = True
                break

        if possible_1:
            sum_1 += result

        if possible_2:
            sum_2 += result

    print(f"Part 1: {sum_1}")
    print(f"Part 2: {sum_2}")


if __name__ == "__main__":
    main()
