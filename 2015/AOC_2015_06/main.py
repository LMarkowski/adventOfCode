def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


data = read_file("data.txt")

grid = [[False for i in range(1000)] for j in range(1000)]

for line in data:
    line = line.split(" ")
    if line[0] == "toggle":
        start = line[1].split(",")
        end = line[3].split(",")
        for i in range(int(start[0]), int(end[0]) + 1):
            for j in range(int(start[1]), int(end[1]) + 1):
                grid[i][j] = not grid[i][j]
    elif line[1] == "on":
        start = line[2].split(",")
        end = line[4].split(",")
        for i in range(int(start[0]), int(end[0]) + 1):
            for j in range(int(start[1]), int(end[1]) + 1):
                grid[i][j] = True
    elif line[1] == "off":
        start = line[2].split(",")
        end = line[4].split(",")
        for i in range(int(start[0]), int(end[0]) + 1):
            for j in range(int(start[1]), int(end[1]) + 1):
                if grid[i][j] > 0:
                    grid[i][j] = False

lights_on = 0

for i in range(1000):
    for j in range(1000):
        if grid[i][j]:
            lights_on += 1

print(lights_on)

grid_2 = [[0 for i in range(1000)] for j in range(1000)]

for line in data:
    line = line.split(" ")
    if line[0] == "toggle":
        start = line[1].split(",")
        end = line[3].split(",")
        for i in range(int(start[0]), int(end[0]) + 1):
            for j in range(int(start[1]), int(end[1]) + 1):
                grid_2[i][j] += 2
    elif line[1] == "on":
        start = line[2].split(",")
        end = line[4].split(",")
        for i in range(int(start[0]), int(end[0]) + 1):
            for j in range(int(start[1]), int(end[1]) + 1):
                grid_2[i][j] += 1
    elif line[1] == "off":
        start = line[2].split(",")
        end = line[4].split(",")
        for i in range(int(start[0]), int(end[0]) + 1):
            for j in range(int(start[1]), int(end[1]) + 1):
                if grid_2[i][j] > 0:
                    grid_2[i][j] -= 1

brightness = 0

for i in range(1000):
    for j in range(1000):
        brightness += grid_2[i][j]

print(brightness)
