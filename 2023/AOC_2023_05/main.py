import time

debug = 1  # 1 for testing | 0 for the final run


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def map_level(level, elements, maps_dict):
    result = []
    for element in elements:
        found = False
        for map in maps_dict[level]:
            if element >= map[1] and element <= map[1] + map[2] - 1:
                result.append(element + map[0] - map[1])
                found = True
        if not found:
            result.append(element)
    return result


def map_level_range(level, ranges, maps_dict):
    result = []
    while ranges:
        r = ranges.pop(0)
        found = False
        for map in maps_dict[level]:
            map_range = (map[1], map[1] + map[2] - 1)
            intersection = range_intersection(r, map_range)
            rest = range_difference(r, map_range)
            difference = map[0] - map[1]
            if intersection:
                new_range = (intersection[0] + difference, intersection[1] + difference)
                result.append(new_range)
                found = True
                ranges.extend(rest)

            if debug:
                print(
                    f"Range: {r} | Map: {map_range}\nIntersection: {intersection} | Rest: {rest}\nDiff: {difference}"
                )
                if intersection:
                    print(f"New range: {new_range}")

                print(f"Result: {result}\n")
        if not found:
            result.append(r)

    return result


def range_intersection(range1: tuple, range2: tuple):
    if range1[0] > range2[1] or range1[1] < range2[0]:
        return None
    else:
        return (max(range1[0], range2[0]), min(range1[1], range2[1]))


def range_difference(set1: tuple, set2: tuple):
    intersection = range_intersection(set1, set2)

    if not intersection:
        return [set1]
    elif set1[0] >= set2[0] and set1[1] <= set2[1]:
        return []
    elif set1[0] == set2[0] and set1[1] == set2[1]:
        return []  # No difference, sets are equal
    elif set1[0] == intersection[0]:
        return [(intersection[1] + 1, set1[1])]
    elif set1[1] == intersection[1]:
        return [(set1[0], intersection[0] - 1)]
    else:
        return [(set1[0], intersection[0] - 1), (intersection[1] + 1, set1[1])]


def range_union(range1: tuple, range2: tuple):
    if range1[1] < range2[0] - 1 or range1[0] > range2[1] + 1:
        return [range1, range2]
    else:
        return [(min(range1[0], range2[0]), max(range1[1], range2[1]))]


def unionize_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    result = []
    for r in ranges:
        if result:
            tmp = result.pop(-1)
            result.extend(range_union(tmp, r))
        else:
            result.append(r)
    return result


def main():
    start_time = time.time()
    data_input = read_file("test-data.txt") if debug else read_file("data.txt")

    seeds = data_input[0].split(":")[1].split()
    seeds = [int(i) for i in seeds]

    ranges = []
    for i in range(0, len(seeds) - 1, 2):
        ranges.append((seeds[i], seeds[i] + seeds[i + 1] - 1))

    data_input = data_input[2:]

    while "" in data_input:
        data_input.remove("")

    maps = [
        "seed-to-soil map:",
        "soil-to-fertilizer map:",
        "fertilizer-to-water map:",
        "water-to-light map:",
        "light-to-temperature map:",
        "temperature-to-humidity map:",
        "humidity-to-location map:",
    ]

    split_data = []
    temp_list = []
    for i in data_input:
        if i in maps:
            if temp_list:
                split_data.append([l.split() for l in temp_list])
            temp_list = []
        else:
            temp_list.append(i)
    split_data.append([l.split() for l in temp_list])

    maps_dict = {}
    for map, data in zip(maps, split_data):
        maps_dict[map.split()[0]] = [[int(i) for i in l] for l in data]

    # part_1
    print("Part 1:")
    print(f"Seeds: {seeds}")
    soils = map_level("seed-to-soil", seeds, maps_dict)
    fertilizers = map_level("soil-to-fertilizer", soils, maps_dict)
    waters = map_level("fertilizer-to-water", fertilizers, maps_dict)
    lights = map_level("water-to-light", waters, maps_dict)
    temperatures = map_level("light-to-temperature", lights, maps_dict)
    humidities = map_level("temperature-to-humidity", temperatures, maps_dict)
    locations = map_level("humidity-to-location", humidities, maps_dict)

    print(f"Locations: {locations}")

    print()
    print(f"Minimum: {min(locations)}")
    print()

    # part_2
    print("Part 2:")
    ranges.sort(key=lambda x: x[0])
    print(f"Seeds ranges: {ranges}")
    print()

    soil_ranges = map_level_range("seed-to-soil", ranges, maps_dict)
    soil_ranges = unionize_ranges(soil_ranges)
    print(f"Soil ranges: {soil_ranges}")
    print()

    fertilizer_ranges = map_level_range("soil-to-fertilizer", soil_ranges, maps_dict)
    fertilizer_ranges = unionize_ranges(fertilizer_ranges)
    print(f"Fertilizer ranges: {fertilizer_ranges}")
    print()

    water_ranges = map_level_range("fertilizer-to-water", fertilizer_ranges, maps_dict)
    water_ranges = unionize_ranges(water_ranges)
    print(f"Water ranges: {water_ranges}")
    print()

    light_ranges = map_level_range("water-to-light", water_ranges, maps_dict)
    light_ranges = unionize_ranges(light_ranges)
    print(f"Light ranges: {light_ranges}")
    print()

    temperature_ranges = map_level_range("light-to-temperature", light_ranges, maps_dict)
    temperature_ranges = unionize_ranges(temperature_ranges)
    print(f"Temperature ranges: {temperature_ranges}")
    print()

    humidity_ranges = map_level_range("temperature-to-humidity", temperature_ranges, maps_dict)
    humidity_ranges = unionize_ranges(humidity_ranges)
    print(f"Humidity ranges: {humidity_ranges}")
    print()

    location_ranges = map_level_range("humidity-to-location", humidity_ranges, maps_dict)
    location_ranges = unionize_ranges(location_ranges)
    print(f"Location ranges: {location_ranges}")

    while (0, 0) in location_ranges:
        location_ranges.remove((0, 0))

    print()
    print(f"Minimum: {min(location_ranges)}")

    # range1 = (81, 94)
    # range2 = (25, 94)

    # print(f"Range 1: {range1}")
    # print(f"Range 2: {range2}")
    # print(f"Union: {range_union(range1, range2)}")
    # print(f"Intersection: {range_intersection(range1, range2)}")
    # print(f"Difference: {range_difference(range1, range2)}")

    # test = [(5,8), (1,2)]
    # test.sort(key=lambda x: x[0])

    # print(f"Test: {test}")

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()


# 137516820
