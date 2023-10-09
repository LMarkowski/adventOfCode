def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


data = read_file("data.txt")

sum = 0
for line in data:
    sum += len(line) - len(eval(line))
print(sum)


def encode(string):
    string = string.replace("\\", "\\\\")
    string = string.replace('"', '\\"')
    return '"' + string + '"'


part_2 = 0

for line in data:
    part_2 += len(encode(line)) - len(line)

print(part_2)
