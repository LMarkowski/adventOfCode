def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def find_marker(signal, buffer_length):
    count = 2
    buffer = [signal[0]]

    for i in range(1, len(signal)):
        buffer.append(signal[i])

        # delete the 1st item so buffer stays the same length
        if len(buffer) > buffer_length:
            del buffer[0]

        # only escape if the buffer reached the expected length and there are no duplicates
        if len(buffer) == buffer_length and len(buffer) == len(set(buffer)):
            break

        count += 1

    return count


def main():
    data = read_file("data.txt")

    print("Part one:", find_marker(data[0], 4))
    print("Part two:", find_marker(data[0], 14))


if __name__ == "__main__":
    main()
