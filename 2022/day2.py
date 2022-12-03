from util import load_input

PLAYS = ["X", "Y", "Z", "A", "B", "C"]

data = load_input(2)
points1 = lambda o, p: 1 + p + 3 * ((p - o - 2) % 3)
points2 = lambda o, p: 3 * p + (o - 1 + (p % 3)) % 3 + 1

for points in [points1, points2]:
    result = sum([points(PLAYS.index(o), PLAYS.index(p)) for o, p in map(str.split, data)])
    print(result)
