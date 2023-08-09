from time import perf_counter as pfc
import re
from collections import defaultdict
import math


def load(file):
  with open(file) as f:
    return [line.strip() for line in f]


def solve():
  f = lambda x: map(int, re.findall('\d+', x))
  outputs, bots, commands = defaultdict(list), defaultdict(list), {}

  for line in load('Tag_10.txt'):
    if line.startswith('value'):
      chip, bot = f(line)
      bots[bot].append(chip)
    else:
      bot_from, dest1, dest2 = f(line)
      t1, t2 = re.findall(' (bot|output)', line)
      commands[bot_from] = (t1, dest1), (t2, dest2)

  while bots:
    for bot in [key for key,value in bots.items() if len(value) == 2]:
      chip1, chip2 = sorted(bots.pop(bot))
      (t1, dest1), (t2, dest2) = commands[bot]
      eval(f'{t1}s[dest1].append(chip1)')
      eval(f'{t2}s[dest2].append(chip2)')
      if chip1 == 17 and chip2 == 61: part1 = bot

  part2 = math.prod(outputs[i][0] for i in range(3))
  return part1, part2


start = pfc()
part1, part2 = solve()
print('Part 1:', part1)
print('Part 2:', part2)
print(pfc() - start)
