def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


class Instruction:
    def __init__(self, cycle, value):
        self.value = value
        self.cycle = cycle

    def __str__(self):
        str = f"addx {self.value}" if self.value != 0 else "noop"
        str += f" at: {self.cycle}"
        return str


def main():
    debug = 0  # 1 for testing | 0 for the final run
    data = read_file("test-data.txt") if debug else read_file("data.txt")
    data_split = [line.split() for line in data]

    instructions_list = []

    message = ""

    for line in data_split:
        if instructions_list:
            first_free_cycle = max([instr.cycle for instr in instructions_list])
        else:
            first_free_cycle = 0

        match line[0]:
            case "addx":
                instructions_list.append(
                    Instruction(first_free_cycle + 2, int(line[1]))
                )
            case "noop":
                instructions_list.append(Instruction(first_free_cycle + 1, 0))

    if debug:
        for instr in instructions_list:
            print(instr)
        print()

    register = 1
    cycle = 1

    interesting_cycles = [20, 60, 100, 140, 180, 220]
    values_to_check = []

    while True:
        cycle += 1

        if debug:
            print(f"Start cycle: {cycle}")
            print(f"Register:    {register}")
            print()

        instr = data_split.pop() if data_split else []

        if cycle in interesting_cycles:
            values_to_check.append(register)

        if debug:
            print(f"End cycle:   {cycle}")

        executed = []
        for instruction in instructions_list:
            if instruction.cycle == cycle:
                register += instruction.value
                executed.append(instruction)

        for item in executed:
            instructions_list.remove(item)

        ####  PRINTING  ####

        if abs((cycle % 40) - register) <= 1:
            message += "#"
        else:
            message += "."

        if cycle % 40 == 0:
            message += "\n"

        #### /PRINTING  ####

        if debug:
            print(f"Register:    {register}")
            print()

        if not instructions_list and not data_split:
            break

    result = 0
    for cycle, register in zip(interesting_cycles, values_to_check):
        result += cycle * register

    if debug:
        print(interesting_cycles)
        print(values_to_check)

    print("Part one:")
    print(result)

    print()

    print("Part two:")
    print(message)


if __name__ == "__main__":
    main()
