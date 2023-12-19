from utils.aoc import get_data_for

data = get_data_for(day=8)

directions = data[0]
mapping = {}

for line in data[2:-1]:
    split = line.split()
    source = split[0]
    left = split[2][1:4]
    right = split[3][:3]
    mapping[source] = [left, right]

current = "AAA"
steps = 0

# part 1

while current != "ZZZ":
    for d in directions:
        if current == "ZZZ":
            break

        if d == "L":
            current = mapping[current][0]
        elif d == "R":
            current = mapping[current][1]
        steps += 1

print(steps)
