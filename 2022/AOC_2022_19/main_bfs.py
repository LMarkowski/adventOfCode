import time

debug = 1  # 1 for testing | 0 for the final run
logging = 0


def read_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data


def main():
    start_time = time.time()
    data = read_file("test-data.txt") if debug else read_file("data.txt")
    data_split = [line.split() for line in data]

    bp = data_split[0]
    bp_qualities = []

    for bp in data_split:
        bp_id = int(bp[1].strip(":"))
        ore_rob_cost_ore = int(bp[6])
        cly_rob_cost_ore = int(bp[12])
        obs_rob_cost_ore = int(bp[18])
        obs_rob_cost_cly = int(bp[21])
        geo_rob_cost_ore = int(bp[27])
        geo_rob_cost_obs = int(bp[30])

        print(f"Blupeprint {bp_id}:")
        print(f"Ore robot:      {ore_rob_cost_ore} ore")
        print(f"Clay robot:     {cly_rob_cost_ore} ore")
        print(f"Obsidian robot: {obs_rob_cost_ore} ore, {obs_rob_cost_cly} clay")
        print(f"Geode robot:    {geo_rob_cost_ore} ore, {geo_rob_cost_obs} obsidian")
        print()

        max_geo = 0

        queue = [(0, 1, 0, 0, 0, 0, 0, 0, 0)]
        explored = []

        while queue:
            state = queue.pop(0)

            mins = state[0]
            if mins == 24:
                if geo > max_geo:
                    max_geo = geo
                continue

            nb_ore_robs = state[1]
            nb_cly_robs = state[2]
            nb_obs_robs = state[3]
            nb_geo_robs = state[4]

            ore = state[5]
            cly = state[6]
            obs = state[7]
            geo = state[8]

            # check possible options
            possible_actions = ["wait"]
            if ore >= ore_rob_cost_ore:
                possible_actions.append("ore")
            if ore >= cly_rob_cost_ore:
                possible_actions.append("cly")
            if ore >= obs_rob_cost_ore and cly >= obs_rob_cost_cly:
                possible_actions.append("obs")
            if ore >= geo_rob_cost_ore and obs >= geo_rob_cost_obs:
                possible_actions.append("geo")

            if nb_ore_robs > 0:  # collect ore
                ore += nb_ore_robs
            if nb_cly_robs > 0:  # collect clay
                cly += nb_cly_robs
            if nb_obs_robs > 0:  # collect obsidian
                obs += nb_obs_robs
            if nb_geo_robs > 0:  # collect geodes
                geo += nb_geo_robs

            if len(possible_actions) > 4 and "wait" in possible_actions:
                possible_actions.remove("wait")

            for action in possible_actions:
                match action:
                    case "wait":
                        pass
                    case "ore":
                        nb_ore_robs += 1
                        ore -= ore_rob_cost_ore
                    case "cly":
                        nb_cly_robs += 1
                        ore -= cly_rob_cost_ore
                    case "obs":
                        nb_obs_robs += 1
                        ore -= obs_rob_cost_ore
                        cly -= obs_rob_cost_cly
                    case "geo":
                        nb_geo_robs += 1
                        ore -= geo_rob_cost_ore
                        obs -= geo_rob_cost_obs
                mins += 1
                new_state = (
                    mins,
                    nb_ore_robs,
                    nb_cly_robs,
                    nb_obs_robs,
                    nb_geo_robs,
                    ore,
                    cly,
                    obs,
                    geo,
                )
                if new_state not in explored:
                    if mins < 25:
                        queue.append(new_state)
                    explored.append(new_state)

        bp_qualities.append(max_geo * bp_id)

    # print(f"Max values: {best_limit}")
    # print()
    # print(f"Ore robots:      {final_nb_ore_robs}")
    # print(f"Clay robots:     {final_nb_cly_robs}")
    # print(f"Obsidian robots: {final_nb_obs_robs}")
    # print(f"Geode robots:    {final_nb_geo_robs}")
    # print()
    # print(f"Ore:      {final_ore}")
    # print(f"Clay:     {final_cly}")
    # print(f"Obsidian: {final_obs}")
    # print(f"Geodes:   {final_geo}")
    # print()
    # print(f"Blueprint quality: {bp_quality}")

    print(bp_qualities)

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
