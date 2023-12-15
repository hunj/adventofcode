from functools import reduce
from utils.aoc import get_data_for

data = get_data_for(day=6)

times = [int(x) for x in data[0].split()[1:]]
distances = [int(x) for x in data[1].split()[1:]]
d = dict(zip(times, distances))

# part 1


def dist(charge_time, min_dist):
    results = []
    for i in range(charge_time):
        moving_time = charge_time - i
        if moving_time * i > min_dist:
            results.append(i)
    return results


res = []
for time, distance in d.items():
    res.append(dist(time, distance))

mult = reduce(lambda a, b: a * b, [len(x) for x in res])
print(mult)

# part 2

x = int(''.join(data[0].split()[1:]))
y = int(''.join(data[1].split()[1:]))

print(len(dist(x, y)))
