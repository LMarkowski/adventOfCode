def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def separate_integers(data):
    result = []
    for line in data:
        result.append([int(char) for char in line])
    return result


def get_all_coords(grid):
    all_coords = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            all_coords.append((i, j))
    return all_coords


def print_grid(matrix):
    for line in matrix:
        for char in line:
            print(char, end="")
        print()
    print()


def print_selected_trees(trees, selected_coords):
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            if (i, j) in selected_coords:
                print(trees[i][j], end="")
            else:
                print(" ", end="")
        print()


def find_visible_trees(grid):
    visible_trees = []

    # ROWS
    for i in range(len(grid)):
        min_left = -1
        min_right = -1

        # LEFT to RIGHT
        for j in range(len(grid[i])):
            if grid[i][j] > min_left:
                visible_trees.append((i, j))
                min_left = grid[i][j]

        # RIGHT to LEFT
        for j in range(len(grid[i]) - 1, -1, -1):
            if grid[i][j] > min_right:
                visible_trees.append((i, j))
                min_right = grid[i][j]

    # COLUMNS
    for j in range(len(grid[0])):
        min_top = -1
        min_bottom = -1

        # TOP to BOTTOM
        for i in range(len(grid)):
            if grid[i][j] > min_top:
                visible_trees.append((i, j))
                min_top = grid[i][j]

        # BOTTOM to TOP
        for i in range(len(grid) - 1, -1, -1):
            if grid[i][j] > min_bottom:
                visible_trees.append((i, j))
                min_bottom = grid[i][j]

    return list(set(visible_trees))


def calculate_scenic_score(tree_coords, grid, debug=False):
    x = tree_coords[0]
    y = tree_coords[1]

    height = grid[x][y]

    top = bottom = right = left = 0

    if debug:
        print("Calculating tree:", tree_coords)
        print("Listing trees visible in all directions:\n")
        print("Top:")
    for i in range(x - 1, -1, -1):
        top += 1
        if debug:
            print(f"({i}, {y}): {grid[i][y]}")
        if grid[i][y] >= height:
            break

    if debug:
        print("Bottom:")
    for i in range(x + 1, len(grid[x]), 1):
        bottom += 1
        if debug:
            print(f"({i}, {y}): {grid[i][y]}")
        if grid[i][y] >= height:
            break

    if debug:
        print("Right:")
    for i in range(y + 1, len(grid), 1):
        right += 1
        if debug:
            print(f"({x}, {i}): {grid[x][i]}")
        if grid[x][i] >= height:
            break

    if debug:
        print("Left:")
    for i in range(y - 1, -1, -1):
        left += 1
        if debug:
            print(f"({x}, {i}): {grid[x][i]}")
        if grid[x][i] >= height:
            break

    score = top * bottom * right * left
    if debug:
        print()
        print("Partial scores:")
        print("Top:   ", top)
        print("Bottom:", bottom)
        print("Right: ", right)
        print("Left:  ", left)
        print()
        print("Total score:", score)

    return score


def find_max_scenic_score(trees):
    max_score = 0
    for tree in get_all_coords(trees):
        score = calculate_scenic_score(tree, trees)
        if score > max_score:
            max_score = score
            best_tree = tree

    return best_tree, max_score


def main():
    debug = False
    data = read_file("test-data.txt") if debug else read_file("data.txt")

    trees = separate_integers(data)
    visible_trees = find_visible_trees(trees)

    if debug:
        print_grid(trees)
        print_selected_trees(trees, visible_trees)
        print()

    if not debug:
        print("Part one:")
        print("Number of visible trees:", len(visible_trees))
        print()

    best_tree, max_score = find_max_scenic_score(trees)

    if not debug:
        print("Part two:")
        print("Coords of the tree with the highest scenic score:", best_tree)
        print("Score:", max_score)

    if debug:
        tree_to_check = best_tree
        print("Score:", calculate_scenic_score(tree_to_check, trees))
        print("Tree:", tree_to_check)
        print("Height:", trees[tree_to_check[0]][tree_to_check[1]])
        print()
        calculate_scenic_score(tree_to_check, trees, True)


if __name__ == "__main__":
    main()
