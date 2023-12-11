from utils import aoc
from functools import reduce
import re

from typing import Dict


data = aoc.get_data_for(day=2)

ids = []
record: Dict[int, Dict[str, int]] = {}

# part 1

for line in data[:-1]:

    current = line[5:]
    re_match = re.match(r'^(\d+): (.*)$', current)
    game_id = int(re_match[1])  # type: ignore

    for match in re_match[2].split(';'):  # type: ignore
        for pair in match.split(','):
            pair = pair.strip()
            pair_re_match = re.match(r'(\d+) (\w+)', pair)
            count, color = int(pair_re_match[1]), pair_re_match[2]  # type: ignore
            if not record.get(game_id):
                record[game_id] = {}
            if not record[game_id].get(color):
                record[game_id][color] = 0
            if record[game_id][color] < count:
                record[game_id][color] = count

for game_id, values in record.items():
    if values['red'] <= 12 and values['green'] <= 13 and values['blue'] <= 14:
        ids.append(game_id)

print(sum(ids))

# part 2

powers = []
for cubes in record.values():
    powers.append(reduce(lambda x, y: x * y, cubes.values()))

print(sum(powers))
