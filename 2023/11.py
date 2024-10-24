from utils.aoc import get_data_for
from itertools import combinations
from pprint import pprint

data = get_data_for(day=11)[:-1]

data = "...#......\
.......#..\
#.........\
..........\
......#...\
.#........\
.........#\
..........\
.......#..\
#...#.....".split()

rows_to_expand, cols_to_expand = [], []

N = len(data)

for row_idx in range(N):
    if len(set(list(data[row_idx]))) == 1:
        rows_to_expand.append(row_idx)
for col_idx in range(N):
    col = [row[col_idx] for row in data]
    if len(set(list(col))) == 1:
        cols_to_expand.append(col_idx)

for row_idx in reversed(rows_to_expand):
    data.insert(row_idx, '.' * N)

for row in data:
    for col_idx in reversed(cols_to_expand):
        row = row[:col_idx] + '.' + row[col_idx:]

galaxy_coordinates = []

for row_idx in range(len(data)):
    for col_idx in range(len(data[row_idx])):
        if data[row_idx][col_idx] == '#':
            galaxy_coordinates.append((row_idx, col_idx))

pairs = combinations(galaxy_coordinates, 2)

# part 1

sum = 0


def dist(coord1, coord2):
    x = coord1[0] - coord2[0] if coord1[0] > coord2[0] else coord2[0] - coord1[0]
    y = coord1[1] - coord2[1] if coord1[1] > coord2[1] else coord2[1] - coord1[1]
    return x + y


for pair in pairs:
    sum += dist(pair[0], pair[1])

print(sum)
