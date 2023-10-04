def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


data = read_file("data.txt")[0]

coords = [(0, 0)]

for char in data[1::2]:
    if char == "^":
        coords.append((coords[-1][0], coords[-1][1] + 1))
    elif char == "v":
        coords.append((coords[-1][0], coords[-1][1] - 1))
    elif char == ">":
        coords.append((coords[-1][0] + 1, coords[-1][1]))
    elif char == "<":
        coords.append((coords[-1][0] - 1, coords[-1][1]))

coords.append((0, 0))

for char in data[::2]:
    if char == "^":
        coords.append((coords[-1][0], coords[-1][1] + 1))
    elif char == "v":
        coords.append((coords[-1][0], coords[-1][1] - 1))
    elif char == ">":
        coords.append((coords[-1][0] + 1, coords[-1][1]))
    elif char == "<":
        coords.append((coords[-1][0] - 1, coords[-1][1]))

print(len(set(coords)))
