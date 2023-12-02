import time

debug = 0  # 1 for testing | 0 for the final run


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def main():
    start_time = time.time()
    data = read_file("test-data.txt") if debug else read_file("data.txt")

    games = {}

    for line in data:
        game = line.split(": ")[0].split(" ")[1]
        sets = line.split(": ")[1].split("; ")
        games[game] = {}
        tmp = {"max_blue": 0, "max_green": 0, "max_red": 0}
        for set in sets:
            colors = set.split(", ")
            for pair in colors:
                color = pair.split(" ")[1]
                nb = int(pair.split(" ")[0])
                if color == "blue" and tmp["max_blue"] < nb:
                    tmp["max_blue"] = nb
                elif color == "green" and tmp["max_green"] < nb:
                    tmp["max_green"] = nb
                if color == "red" and tmp["max_red"] < nb:
                    tmp["max_red"] = nb
        games[game] = tmp

    if debug:
        for game in games:
            print(f"Game {game}: {games[game]}")

    balls = {"blue": 14, "green": 13, "red": 12}
    possibleGames = 0

    for game in games:
        if (
            games[game]["max_blue"] <= balls["blue"]
            and games[game]["max_green"] <= balls["green"]
            and games[game]["max_red"] <= balls["red"]
        ):
            possibleGames += int(game)

    powers = 0
    for game in games:
        powers += games[game]["max_blue"] * games[game]["max_green"] * games[game]["max_red"]

    print(f"Possible games: {possibleGames}")

    print(f"Power: {powers}")

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
