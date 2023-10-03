def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


class Valve:
    def __init__(self, line):
        self.id = line[1]
        self.flow = int(line[4][5:-1])
        self.paths = [path.strip(",") for path in line[9:]]
        self.opened = True if not self.flow else False

    def __str__(self):
        return f"{self.id}, {self.flow}, {self.paths}, {self.opened}"

    def open(self):
        if self.opened:
            return 0
        else:
            return 1


def go(valve_to, valves):
    global pos
    if valve_to not in pos.paths:
        print("There is no direct path")
        return 0
    else:
        pos = valves[valve_to]
        return 1


global pos


def main():
    debug = 1  # 1 for testing | 0 for the final run
    data = read_file("test-data.txt") if debug else read_file("data.txt")
    data_split = [line.split() for line in data]

    global pos

    valves = {}

    for line in data_split:
        valves[line[1]] = Valve(line)

    pos = valves[0]
    minutes = 0
    total_flow = 0
    for valve in valves:
        print(valve)

    add_time = pos.open()
    if add_time == 1:
        total_flow += pos.flow

    print(f"Current position: {pos.id}")
    print(f"Possible paths:   {pos.paths}")
    print(f"Current flow:     {total_flow}")


if __name__ == "__main__":
    main()
