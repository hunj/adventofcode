from utils import aoc

data = aoc.get_data_for(day=4)


def score(winning, numbers):
    points = 0
    for num in numbers:
        if num in winning:
            points = points * 2 if points else 1

    return points


sum_score = 0

for line in data:
    if not line:
        break

    split_line = line[5:].split('|')
    winners = split_line[0].split()[1:]
    numbers = split_line[1].split()

    sum_score += score(winners, numbers)

print(sum_score)
