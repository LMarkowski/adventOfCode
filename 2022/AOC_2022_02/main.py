def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


possible_wins = {"C": "X", "A": "Y", "B": "Z"}

possible_draws = {"A": "X", "B": "Y", "C": "Z"}

possible_losses = {"B": "X", "C": "Y", "A": "Z"}

shape_scores = {"X": 1, "Y": 2, "Z": 3}


def calculate_score(data):
    total_score = 0
    for game in data:
        total_score += shape_scores[game[1]]
        if possible_wins[game[0]] == game[1]:
            total_score += 6
        elif possible_draws[game[0]] == game[1]:
            total_score += 3
    return total_score


def adjust_data(data):
    adjusted_data = []
    for game in data:
        tmp = [game[0]]
        if game[1] == "X":  # need to loose
            tmp.append(possible_losses[game[0]])
        elif game[1] == "Y":  # need to draw
            tmp.append(possible_draws[game[0]])
        else:  # need to win
            tmp.append(possible_wins[game[0]])
        adjusted_data.append(tmp)
    return adjusted_data


def main():
    data = read_file("data.txt")
    data_split = [line.split(" ") for line in data]

    first_strategy = calculate_score(data_split)
    print(f"First score: {first_strategy}")
    second_strategy = calculate_score(adjust_data(data_split))
    print(f"Second score: {second_strategy}")


if __name__ == "__main__":
    main()
