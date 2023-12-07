import time
from itertools import product

debug = 0  # 1 for testing | 0 for the final run


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def assign_type(hand, deck):
    counts = {}
    for card in deck:
        counts[card] = hand.count(card)
    max_count = max(counts.values())
    if max_count == 5:
        return 6
    elif max_count == 4:
        return 5
    elif max_count == 3:
        if 2 in counts.values():
            return 4
        else:
            return 3
    elif max_count == 2:
        if list(counts.values()).count(2) == 2:
            return 2
        else:
            return 1
    else:
        return 0


def exchange_jokers(hand, deck, alphabet):
    if "J" not in hand:
        return hand
    J_count = hand.count("J")
    combinations = list(product(deck, repeat=J_count))
    tmp = []
    for combination in combinations:
        temp_str = hand
        for char in combination:
            temp_str = temp_str.replace("J", char, 1)
        tmp.append(temp_str)

    if debug:
        print(tmp)
    sorted_tmp = sorted(tmp, key=lambda x: (assign_type(x, deck), [alphabet.index(c) for c in x]))
    return sorted_tmp[-1]


def main():
    start_time = time.time()
    data = read_file("test-data.txt") if debug else read_file("data.txt")

    deck = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    deck.reverse()
    alphabet = "".join(deck)

    powers = {
        0: "Nothing",
        1: "One pair",
        2: "Two pairs",
        3: "Three of a kind",
        4: "Full house",
        5: "Four of a kind",
        6: "Five of a kind",
    }

    hands = []
    for line in data:
        line_split = line.split()
        enhanced_hand = exchange_jokers(line_split[0], deck, alphabet)
        hands.append((line_split[0], enhanced_hand, line_split[1]))

    sorted_part_1 = sorted(
        hands, key=lambda x: (assign_type(x[0], deck), [alphabet.index(c) for c in x[0]])
    )
    sorted_part_2 = sorted(
        hands, key=lambda x: (assign_type(x[1], deck), [alphabet.index(c) for c in x[0]])
    )

    sum_part_1 = 0
    sum_part_2 = 0

    for i in range(len(hands)):
        sum_part_1 += int(sorted_part_1[i][2]) * (i + 1)
        sum_part_2 += int(sorted_part_2[i][2]) * (i + 1)

    print(f"Part 1: {sum_part_1}")
    print(f"Part 2: {sum_part_2}")

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
