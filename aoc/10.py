from utils.aoc import get_data_for

data = get_data_for(day=10)[:-1]


"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

START = (None, None)
MATRIX = {}  # (row, col) => [(row, col) ... ]
NUM_ROWS = len(data)
NUM_COLS = len(data[0])


def add_slot_if_need(row, col):
    if (row, col) not in MATRIX:
        MATRIX[(row, col)] = []


def add_north(row, col):
    if row > 0:
        add_slot_if_need(row, col)
        MATRIX[(row, col)].append((row - 1, col))


def add_south(row, col):
    if row < NUM_ROWS - 1:
        add_slot_if_need(row, col)
        MATRIX[(row, col)].append((row + 1, col))


def add_west(row, col):
    if col > 0:
        add_slot_if_need(row, col)
        MATRIX[(row, col)].append((row, col - 1))


def add_east(row, col):
    if col < NUM_COLS - 1:
        add_slot_if_need(row, col)
        MATRIX[(row, col)].append((row, col + 1))


# set up adjacency matrix
for row in range(len(data)):
    length = len(data[row])
    for col in range(length):
        match data[row][col]:
            case "|":
                add_north(row, col)
                add_south(row, col)

            case "-":
                add_west(row, col)
                add_east(row, col)

            case "L":
                add_north(row, col)
                add_east(row, col)

            case "J":
                add_north(row, col)
                add_west(row, col)

            case "7":
                add_south(row, col)
                add_west(row, col)

            case "F":
                add_south(row, col)
                add_east(row, col)

            case "S":
                START = (row, col)
                MATRIX[START] = []

for coordinate, neighbors in MATRIX.items():
    if START in neighbors:
        MATRIX[START].append(coordinate)

DISTANCES = {}
to_visit = MATRIX[START]
for start in to_visit:
    DISTANCES[start] = 1

# part 1; breadth first search

while to_visit:
    current = to_visit.pop(0)

    for next in MATRIX[current]:
        if next not in DISTANCES:
            DISTANCES[next] = DISTANCES[current] + 1
            to_visit.append(next)

print(max(DISTANCES.values()))
