from utils.aoc import get_data_for

data = [list(map(lambda x: int(x), line.split())) for line in get_data_for(day=9)[:-1]]



def diff_each_step(steps):
    diff = []
    for i in range(1, len(steps)):
        diff.append(steps[i] - steps[i-1])
    return diff


def diff_all(acc, line):
    diff = diff_each_step(line)
    acc.append(diff)
    if any(diff):
        diff_all(acc, diff)
    return acc


# part 1

def extrapolated_value_by_appending(history):
    for idx in reversed(range(len(history))):
        if idx == len(history)-1:
            history[idx].append(0)
        else:
            to_append = history[idx][-1] + history[idx + 1][-1]
            history[idx].append(to_append)
    return history


sum = 0
for line in data:
    current = diff_all([], line)
    x = extrapolated_value_by_appending(current)[0][-1]
    sum += line[-1] + x

print(sum)


# part 2

def extrapolated_value_by_prepending(history):
    for idx in reversed(range(len(history))):
        if idx == len(history)-1:
            history[idx].insert(0, 0)
        else:
            to_append = history[idx][0] - history[idx + 1][0]
            history[idx].insert(0, to_append)
    return history

sum = 0
for line in data:
    current = diff_all([], line)
    x = extrapolated_value_by_prepending(current)[0][0]
    line.insert(0, line[0] - x)
    sum += line[0]

print(sum)
