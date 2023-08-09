from time import perf_counter as pfc
import re


def load(file):
  with open(file) as f:
    return [re.split(r'\[([^\]]+)\]', line.strip()) for line in f]


def abba(x, part2=False):
  pattern = r'(?=((.)(?!\2).\2))' if part2 else r'(.)(?!\1)(.)\2\1'
  return re.search(pattern, x) != None


start = pfc()
puzzle = load('Tag_07.txt')
parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in puzzle]


print('Part 1:', sum(abba(sn) and not (abba(hn)) for sn, hn in parts))
print('Part 2:', sum(any(a == c and a != b and b+a+b in hn
                         for a, b, c in zip(sn, sn[1:], sn[2:]))
                         for sn, hn in parts))
print(pfc() - start)
