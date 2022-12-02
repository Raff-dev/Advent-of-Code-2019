from itertools import groupby

from util import load_input

data = load_input(1)
result = max([sum(map(int, g)) for k, g in groupby(data, key=bool) if k])
print(result)
