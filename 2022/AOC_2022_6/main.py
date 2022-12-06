def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def find_marker(signal, buffer_length):
    buffer = list(signal[:buffer_length])
    count = buffer_length

    for i in range(buffer_length, len(signal)):
        buffer.append(signal[i])
        del buffer[0]  # remove 1st charachter so the buffer stays the same length
        count += 1

        # check for duplicates
        if len(buffer) == len(set(buffer)):
            break

    return count


def main():
    data = read_file("data.txt")

    print("Part one:", find_marker(data[0], 4))
    print("Part two:", find_marker(data[0], 14))


if __name__ == "__main__":
    main()
