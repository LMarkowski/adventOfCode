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
        if entry == sep and tmp:
            result.append(tmp)
            tmp = []
        else:
            tmp.append(entry)
    if tmp:
        result.append(tmp)
    return result


class Monkey:
    def __init__(self, monkey_data):
        self.id = int(monkey_data[0].split(" ")[1][:-1])
        self.items = self.__parse_items(monkey_data[1].split(":")[1])
        self.operation = self.__parse_operation(monkey_data[2])
        self.test = int(monkey_data[3].split()[-1])
        self.if_true = int(monkey_data[4].split()[-1])
        self.if_false = int(monkey_data[5].split()[-1])
        self.items_checked = 0

    def __str__(self):
        result = f"{self.id}\n"
        result += f"items: {self.items}\n"
        result += f"operation: {self.operation}\n"
        result += f"test: divisable by {self.test}\n"
        result += f"if true throw to: {self.if_true}\n"
        result += f"if false throw to: {self.if_false}\n"
        return result

    def __parse_items(self, string):
        values = string.strip().split(",")
        return [int(item.strip()) for item in values]

    def __parse_operation(self, string):
        values = string.strip().split(" ")
        return values[-2:]

    def change_item(self, item):
        factor = item if self.operation[1] == "old" else int(self.operation[1])
        if self.operation[0] == "*":
            worry_level = item * factor
        else:
            worry_level = item + factor
        
        self.items_checked += 1
        if part_one:
            return worry_level // 3
        else:
            return worry_level % total_modulo

    def throw_to(self, item):
        if int(item % self.test) == 0:
            return self.if_true
        else:
            return self.if_false

debug = 0  # 1 for testing | 0 for the final run
logging = 0
part_one = 0
total_modulo = 1

def main():
    data = read_file("test-data.txt") if debug else read_file("data.txt")
    monkeys_data = split_list([line.strip() for line in data], "")
    monkeys = [Monkey(monkey_data) for monkey_data in monkeys_data]
    round = 0
    global total_modulo

    break_round = 20 if part_one else 10000

    for monkey in monkeys:
        total_modulo *= monkey.test

    while True:
        round += 1

        if logging:
            print(f"Start round: {round}")

        for monkey in monkeys:
            if logging:
                print(f"Monkey {monkey.id}")
            for item in monkey.items:
                new_item = monkey.change_item(item)
                throwing_to = monkey.throw_to(new_item)
                if logging:
                    print(f"{item} -> {new_item} | throwing to {throwing_to}")
                monkeys[throwing_to].items.append(new_item)
            monkey.items = []

        if logging:
            print(f"End round: {round}\n")

        if round == break_round:
            break
     
    for monkey in monkeys:
        print(f"Monkey {monkey.id}")
        print(f"Inspected: {monkey.items_checked}")
        print()

    inspectors = [m.items_checked for m in monkeys]
    inspectors.sort()

    print(f"Final result:\n{inspectors[-1] * inspectors[-2]}")


if __name__ == "__main__":
    main()
