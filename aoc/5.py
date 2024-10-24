from utils import aoc

data = aoc.get_data_for(day=5)

seeds = data[1].split()[1:]

"""
seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location
"""

soil = dict.fromkeys(seeds)
fert, water, light, temp, humid, loc = {}, {}, {}, {}, {}, {}

to_parse = data[2:]
while to_parse:
    line = to_parse.pop(0)
    if line.startswith("seed-to-soil"):
        line = to_parse.pop(0)  # remove header line
        while line:
            line = to_parse.pop(0)
            if map := line.split():
                if len(map) == 3:
                    destination, source, length = [int(x) for x in map]
                    for i in range(length):
                        soil[source + i] = destination + i
                    print(soil)

    # if line.startswith("soil-to-fertilizer")

print(soil)
