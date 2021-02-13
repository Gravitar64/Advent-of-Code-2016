from time import perf_counter as pfc
from collections import Counter


def load(file):
  with open(file) as f:
    return [x.strip() for x in f]


def solve(p):
  part1 = ''.join((Counter(a).most_common()[0][0] for a in zip(*p)))
  part2 = ''.join((Counter(a).most_common()[-1][0] for a in zip(*p)))
  return part1, part2


puzzle = load('Tag_06.txt')

start = pfc()
print(solve(puzzle), pfc() - start)
