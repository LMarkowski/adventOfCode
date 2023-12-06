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

    cards = {}

    for line in data:
        split_1 = line.split(":")
        split_2 = split_1[1].split(" | ")
        winning = list(map(int, split_2[0].split()))
        have = list(map(int, split_2[1].split()))

        cards[int(split_1[0].split()[1])] = {
            "win": winning,
            "had": have,
        }

    sum = 0

    for key, value in cards.items():
        if debug:
            print(f"Game {key}")
            print(f"Winning: {value['win']}")
            print(f"had: {value['had']}")
        matches = 0
        for number in value["had"]:
            if number in value["win"]:
                matches += 1
        adding = 0
        if matches > 0:
            adding = 2 ** (matches - 1)

        sum += adding

    print(f"Points: {sum}")

    nb_of_cards = {}
    for key in cards.keys():
        nb_of_cards[key] = 1

    for key, value in cards.items():
        matches = 0
        for number in value["had"]:
            if number in value["win"]:
                matches += 1

        for i in range(key + 1, key + 1 + matches):
            nb_of_cards[i] = nb_of_cards.get(i, 0) + nb_of_cards[key]

    total_cards = 0
    for key, value in nb_of_cards.items():
        # print(f"{key}: {value}")
        total_cards += value
    print(f"Total cards: {total_cards}")

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
