def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


class Instruction:
    # Could as well be a tuple, but this way seems to be more clear
    # Attributes:
    #   value: value to be added to the registry
    #   cycle: cycle in which this instruction will be executed

    def __init__(self, cycle: int, value: int):
        self.value = value
        self.cycle = cycle

    def __str__(self):
        str = f"addx {self.value}" if self.value != 0 else "noop"
        str += f" at: {self.cycle}"
        return str


def make_instructions_queue(data):
    instructions_list = []

    for line in data:
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

    return instructions_list


def get_part_one_result(interesting_cycles, values_to_check):
    result = 0
    for cycle, register in zip(interesting_cycles, values_to_check):
        result += cycle * register
    return result


def main():
    debug = 0  # 1 for testing | 0 for the final run
    data = read_file("test-data.txt") if debug else read_file("data.txt")
    data_split = [line.split() for line in data]

    instructions_queue = make_instructions_queue(data_split)

    if debug:
        for instr in instructions_queue:
            print(instr)
        print()

    register = 1
    cycle = 0
    message = ""

    interesting_cycles = [20, 60, 100, 140, 180, 220]
    values_to_check = []

    while True:
        cycle += 1

        if debug:
            print(f"Start cycle: {cycle}")
            print(f"Register:    {register}")

        if cycle in interesting_cycles:
            values_to_check.append(register)

        executed = []
        for instruction in instructions_queue:
            if instruction.cycle == cycle:
                register += instruction.value
                executed.append(instruction)

        for item in executed:
            instructions_queue.remove(item)

        ####  PRINTING  ####

        if abs((cycle % 40) - (register)) <= 1:
            message += "█"
        else:
            message += " "

        if cycle % 40 == 0:
            message += "\n"

        #### /PRINTING  ####

        if debug:
            print(f"End cycle:   {cycle}")
            print(f"Register:    {register}")
            print()

        if not instructions_queue:
            break

    if debug:
        print(interesting_cycles)
        print(values_to_check)
        print()

    result = get_part_one_result(interesting_cycles, values_to_check)

    print("Part one:")
    print(result)

    print()

    print("Part two:")
    print(message)


if __name__ == "__main__":
    main()
