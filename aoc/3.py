from utils import aoc
from string import digits

data = aoc.get_data_for(day=3)

print(data)

def is_symbol(char):
    return char != '.' and char not in digits

for line in data:
