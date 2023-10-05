def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


data = read_file("data.txt")

data = [x.split(" -> ") for x in data]

operators = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]

wires = {}

for line in data:
    if line[0].isdigit():
        wires[line[1]] = int(line[0])
    else:
        wires[line[1]] = line[0]

wires["b"] = 956


known_wires = {}

# copilot helped but did not give immediate the answer


def get_value(wire):
    if wire in known_wires:
        return known_wires[wire]

    if wire in wires:
        if type(wires[wire]) == int:
            known_wires[wire] = wires[wire]
            return wires[wire]
        elif wires[wire].isdigit():
            known_wires[wire] = wires[wire]
            return int(wires[wire])
        else:
            if "AND" in wires[wire]:
                value = get_value(wires[wire].split(" ")[0]) & get_value(wires[wire].split(" ")[2])
            elif "OR" in wires[wire]:
                value = get_value(wires[wire].split(" ")[0]) | get_value(wires[wire].split(" ")[2])
            elif "LSHIFT" in wires[wire]:
                value = get_value(wires[wire].split(" ")[0]) << get_value(wires[wire].split(" ")[2])
            elif "RSHIFT" in wires[wire]:
                value = get_value(wires[wire].split(" ")[0]) >> get_value(wires[wire].split(" ")[2])
            elif "NOT" in wires[wire]:
                value = ~get_value(wires[wire].split(" ")[1])
            else:
                return get_value(wires[wire])
            known_wires[wire] = value
            return value
    else:
        return int(wire)


print(get_value("a"))
