import time
from math import lcm

debug = 0  # 1 for testing | 0 for the final run


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def all_done(nodes):
    for node in nodes:
        if node[2] != "Z":
            return False
    return True


def main():
    start_time = time.time()
    data = read_file("test-data.txt") if debug else read_file("data.txt")

    instructions = data[0]

    nodes_data = data[2:]
    nodes = {}
    for line in nodes_data:
        line = line.split(" = ")
        coords = line[1][1:-1].split(", ")
        nodes[line[0]] = (coords[0], coords[1])

    # Part 1
    current_node = "AAA"
    destination_node = "ZZZ"

    steps = 0
    if debug:
        print(current_node)
    while current_node != destination_node:
        if instructions[steps % len(instructions)] == "R":
            current_node = nodes[current_node][1]
        else:
            current_node = nodes[current_node][0]
        if debug:
            print(current_node)
        steps += 1

    print(f"Part 1: {steps}")

    # Part 2
    current_nodes = []
    for node in nodes.keys():
        if node[2] == "A":
            current_nodes.append(node)
    if debug:
        print(current_nodes)

    steps_list = []
    for start in current_nodes:
        steps = 0
        current = start
        while current[2] != "Z":
            if instructions[steps % len(instructions)] == "R":
                current = nodes[current][1]
            else:
                current = nodes[current][0]
            steps += 1
        steps_list.append(steps)
    if debug:
        print(steps_list)

    print(f"Part_2: {lcm(*steps_list)}")

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
