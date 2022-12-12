def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def __str__(self):
        return f"({self.x}, {self.y}) {'(has parent)' if self.parent is not None else '(root)'}"


def print_grid(grid):
    for line in grid:
        for char in line:
            print(char, end="")
        print()


def print_on_grid(list, grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            flag = False
            for point in list:
                if point.x == x and point.y == y:
                    print("#", end="")
                    flag = True
            if not flag:
                print(" ", end="")
        print()
    print()


def compare_chars(char, other):
    if char == "S":
        char = "a"

    if other == "E":
        other = "z"

    if ord(other) <= ord(char) + 1:
        return True
    else:
        return False


def possible_paths(field, grid):
    result = []
    x = field.x
    y = field.y
    elev = grid[x][y]

    if x < len(grid) - 1 and compare_chars(elev, grid[x + 1][y]):
        result.append(Node(x + 1, y))
    if y < len(grid[x]) - 1 and compare_chars(elev, grid[x][y + 1]):
        result.append(Node(x, y + 1))
    if x > 0 and compare_chars(elev, grid[x - 1][y]):
        result.append(Node(x - 1, y))
    if y > 0 and compare_chars(elev, grid[x][y - 1]):
        result.append(Node(x, y - 1))

    return result


def goal(field, grid):
    return True if grid[field.x][field.y] == "E" else False


def path_from_start(node: Node):
    path = []
    while node.parent is not None:
        path.append(node)
        node = node.parent
    return path


def bfs(start, grid):
    queue = [start]
    explored_coords = [(queue[0].x, queue[0].y)]

    end = None
    # Breadth-first search alorithm
    while queue:
        current = queue.pop(0)
        if goal(current, grid):
            if logging:
                print(f"found E at: {current}")
            end = current
        for next in possible_paths(current, grid):
            if (next.x, next.y) not in explored_coords:
                explored_coords.append((next.x, next.y))
                next.parent = current
                queue.append(next)

    if end:
        path = path_from_start(end)
        return len(path)
    else:
        return 1000


debug = 0  # 1 for testing | 0 for the final run
logging = 0
part_one = 1


def main():
    data = read_file("test-data.txt") if debug else read_file("data.txt")
    grid = [list(line) for line in data]

    paths = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "a":
                paths.append(bfs(Node(i, j), grid))
                print(len(paths))

    if logging:
        print_grid(grid)
        print()
        print_on_grid(path, grid)

    print(f"Reached summit in {min(paths)} steps")


if __name__ == "__main__":
    main()
