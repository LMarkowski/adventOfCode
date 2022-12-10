def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


class Line:
    def __init__(self, length):
        self.nodes = [Node(None, 0, 0)]
        for i in range(0, length - 1):
            self.nodes.append(Node(self.nodes[i], 0, 0))

    def __str__(self):
        result = ""
        for node in self.nodes:
            result += f"{node}\n"
        return result

    def tail(self):
        return self.nodes[-1]

    def get_all_coords(self):
        return [node.get_pos() for node in self.nodes]


class Node:
    def __init__(self, head, x, y):
        self.head = head
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y}) {'HEAD' if self.head is None else ''}"

    def __move(self, x, y):
        self.x += x
        self.y += y

    def move(self, direction):
        if self.head is None:
            match direction:
                case "R":
                    self.__move(1, 0)
                case "L":
                    self.__move(-1, 0)
                case "U":
                    self.__move(0, 1)
                case "D":
                    self.__move(0, -1)
        else:
            self.follow_head()

    def get_pos(self):
        return self.x, self.y

    def follow_head(self):
        vector = (self.head.x - self.x, self.head.y - self.y)

        if abs(vector[0]) == 2 and abs(vector[1]) == 2:
            self.__move(vector[0] // 2, vector[1] // 2)
        elif abs(vector[0]) == 2:
            self.__move(vector[0] // 2, 0)
            self.y = self.head.y
        elif abs(vector[1]) == 2:
            self.__move(0, vector[1] // 2)
            self.x = self.head.x


def print_on_grid(list):
    for x in range(-12, 12):
        for y in range(-12, 12):
            if x == 0 and y == 0:
                print("s", end="")
            elif (y, -x) in list:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def main():
    debug = 0  # 1 for testing | 0 for final run
    data = read_file("test-data.txt") if debug else read_file("data.txt")
    data_split = [line.split() for line in data]
    steps = []
    for line in data_split:
        for i in range(int(line[1])):
            steps.append(line[0])

    # create the line
    line_length = 10
    line = Line(line_length)

    # initialize tail path
    tail_path = [line.tail().get_pos()]

    # run the instructions
    for step in steps:
        for node in line.nodes:
            node.move(step)
        tail_path.append(line.tail().get_pos())

    line_coords = line.get_all_coords()

    # print_on_grid(line_coords)
    # print_on_grid(tail_path)
    # print(line)

    print("Answer:", len(set(tail_path)))


if __name__ == "__main__":
    main()
