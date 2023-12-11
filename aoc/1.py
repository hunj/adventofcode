import re
from utils import aoc

data = aoc.get_data_for(day=1)

# part 1

SUM = 0

for line in data:
    re_match = re.findall(r'\d', line)
    if not re_match:
        continue
    to_add = int(re_match[0]) * 10 + int(re_match[-1])

    SUM += to_add

print(SUM)
