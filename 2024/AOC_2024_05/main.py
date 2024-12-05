def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def check_update(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) < update.index(rule[1]):
                pass
            else:
                print(f"Broke rule: {rule[0]}|{rule[1]}")
                return False
    return True


def fix_update(update, rules):
    while not check_update(update, rules):
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                index_1 = update.index(rule[0])
                index_2 = update.index(rule[1])
                update[min(index_1, index_2)] = rule[0]
                update[max(index_1, index_2)] = rule[1]
    return update


def main():
    data = read_file("input.txt")

    rules = []
    updates = []

    for line in data:
        if "|" in line:
            rules.append(line.split("|"))
        if "," in line:
            updates.append(line.split(","))

    sum = 0
    sum_2 = 0

    for update in updates:
        print(f"Checking update: {update}")
        if check_update(update, rules):
            print("Update is valid")
            middle_page = update[len(update) // 2]
            sum += int(middle_page)
            print()
        else:
            print("Update is invalid")
            print("Fixing update")
            update = fix_update(update, rules)
            print(f"Fixed update: {update}")
            middle_page = update[len(update) // 2]
            sum_2 += int(middle_page)
            print()

    print(f"Sum: {sum}")
    print(f"Sum 2: {sum_2}")


if __name__ == "__main__":
    main()
