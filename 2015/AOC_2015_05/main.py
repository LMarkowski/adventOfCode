def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


data = read_file("data.txt")

vowels = "aeiou"
bad_strings = ["ab", "cd", "pq", "xy"]


def is_nice(string):
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    if vowel_count < 3:
        return False
    for bad_string in bad_strings:
        if bad_string in string:
            return False
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False


nice_strings = 0

for string in data:
    if is_nice(string):
        nice_strings += 1

print(nice_strings)


def is_nice_2(string):
    for i in range(len(string) - 3):
        if string[i : i + 2] in string[i + 2 :]:
            break
    else:
        return False
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True
    return False


nice_strings_2 = 0

for string in data:
    if is_nice_2(string):
        nice_strings_2 += 1

print(nice_strings_2)
