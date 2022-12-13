from functools import cmp_to_key


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def make_pairs(list):
    pairs = []
    for i in range(len(list) // 3 + 1):
        pairs.append((eval(list[3 * i]), eval(list[3 * i + 1])))
    return pairs


def list_all(list):
    all = []
    for line in list:
        if line != "":
            all.append(eval(line))
    return all


def compare_lists(left, right):
    if logging:
        print(f"entered with {left} vs {right}")
    # if len(left) == 0:
    #     if logging:
    #         print("True by list length")
    #     return True

    for l, r in zip(left, right):
        if logging:
            print(f"{l} vs {r}")
        if type(l) is int and type(r) is int:
            if l < r:
                if logging:
                    print("True by comparison")
                return True
            elif l > r:
                if logging:
                    print("False by comparison")
                return False
        elif type(l) is list and type(r) is list:
            tmp = compare_lists(l, r)
            if tmp is not None:
                return tmp
        elif type(l) is int and type(r) is list:
            tmp = compare_lists([l], r)
            if tmp is not None:
                return tmp
        elif type(l) is list and type(r) is int:
            tmp = compare_lists(l, [r])
            if tmp is not None:
                return tmp

    if len(left) < len(right):
        if logging:
            print("True by list length")
        return True

    if len(left) > len(right):
        if logging:
            print("False by list length")
        return False


def mycmp(a, b):
    if compare_lists(a, b):
        return -1
    else:
        return 1


debug = 0  # 1 for testing | 0 for the final run
logging = 0


def main():
    data = read_file("test-data.txt") if debug else read_file("data.txt")
    pairs = make_pairs(data)
    all = list_all(data)

    correct = []
    counter = 1
    for pair in pairs:
        if logging:
            print("PAIR", counter)
        is_correct = compare_lists(pair[0], pair[1])
        if is_correct:
            correct.append(counter)
        if logging:
            print(is_correct, "\n")
        counter += 1

    # print("Correct indices:", correct)
    print("Part one:", sum(correct))

    all.append([[2]])
    all.append([[6]])

    sorted_all = sorted(all, key=cmp_to_key(mycmp))
    # print(sorted_all)
    print("Part two:", (sorted_all.index([[2]]) + 1) * (sorted_all.index([[6]]) + 1))


if __name__ == "__main__":
    main()

# 5410 too high
