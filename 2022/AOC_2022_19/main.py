import time

debug = 1  # 1 for testing | 0 for the final run
logging = 1


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

    options = []

    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                options.append((i, j, k))

    options = [(1, 4, 2)]

    bp_quality = 0
    for limit in options:
        nb_ore_robs = 1
        nb_cly_robs = 0
        nb_obs_robs = 0
        nb_geo_robs = 0

        ore = 0
        cly = 0
        obs = 0
        geo = 0

        for _ in range(24):
            if logging:
                print(f"Minute {_ + 1}")
                print()

            build_ore_rob = False
            build_cly_rob = False
            build_obs_rob = False
            build_geo_rob = False

            # start building ore robot
            if nb_ore_robs < limit[0]:
                if ore >= ore_rob_cost_ore:
                    if logging:
                        print("Built 1 ore robot.\n")
                    build_ore_rob = True
                    ore -= ore_rob_cost_ore

            # start building clay robot
            if nb_cly_robs < limit[1]:
                if ore >= cly_rob_cost_ore:
                    if logging:
                        print("Built 1 clay robot.\n")
                    build_cly_rob = True
                    ore -= cly_rob_cost_ore

            # start building obsidian robot
            if nb_obs_robs < limit[2]:
                if ore >= obs_rob_cost_ore and cly >= obs_rob_cost_cly:
                    if logging:
                        print("Built 1 obsidian robot.\n")
                    build_obs_rob = True
                    ore -= obs_rob_cost_ore
                    cly -= obs_rob_cost_cly

            # start building geode robot
            if ore >= geo_rob_cost_ore and obs >= geo_rob_cost_obs:
                if logging:
                    print("Built 1 geode robot.\n")
                build_geo_rob = True
                ore -= geo_rob_cost_ore
                obs -= geo_rob_cost_obs

            if nb_ore_robs > 0:  # collect ore
                ore += nb_ore_robs
            if nb_cly_robs > 0:  # collect clay
                cly += nb_cly_robs
            if nb_obs_robs > 0:  # collect obsidian
                obs += nb_obs_robs
            if nb_geo_robs > 0:  # collect geodes
                geo += nb_geo_robs

            if logging:
                print(f"Ore robots:      {nb_ore_robs}")
                print(f"Clay robots:     {nb_cly_robs}")
                print(f"Obsidian robots: {nb_obs_robs}")
                print(f"Geode robots:    {nb_geo_robs}")
                print()
                print(f"Ore:      {ore}")
                print(f"Clay:     {cly}")
                print(f"Obsidian: {obs}")
                print(f"Geodes:   {geo}")
                print()

            if build_ore_rob:  # build ore robots
                nb_ore_robs += 1
            if build_cly_rob:  # build clay robots
                nb_cly_robs += 1
            if build_obs_rob:  # build obsidian robots
                nb_obs_robs += 1
            if build_geo_rob:  # build geode robots
                nb_geo_robs += 1

        check = geo * bp_id
        if check > bp_quality:
            bp_quality = check
            best_limit = limit
            final_nb_ore_robs = nb_ore_robs
            final_nb_cly_robs = nb_cly_robs
            final_nb_obs_robs = nb_obs_robs
            final_nb_geo_robs = nb_geo_robs
            final_ore = ore
            final_cly = cly
            final_obs = obs
            final_geo = geo

    print(f"Max values: {best_limit}")
    print()
    print(f"Ore robots:      {final_nb_ore_robs}")
    print(f"Clay robots:     {final_nb_cly_robs}")
    print(f"Obsidian robots: {final_nb_obs_robs}")
    print(f"Geode robots:    {final_nb_geo_robs}")
    print()
    print(f"Ore:      {final_ore}")
    print(f"Clay:     {final_cly}")
    print(f"Obsidian: {final_obs}")
    print(f"Geodes:   {final_geo}")
    print()
    print(f"Blueprint quality: {bp_quality}")

    print(f"\nFinished in {round(time.time() - start_time, 5)} seconds.")


if __name__ == "__main__":
    main()
