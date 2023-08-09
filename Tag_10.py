from time import perf_counter as pfc
import re
from collections import defaultdict
import math


def load(file):
  with open(file) as f:
    return [line.strip() for line in f]


def solve():
  output, bot, commands = defaultdict(list), defaultdict(list), {}

  for line in load('Tag_10.txt'):
    if line.startswith('value'):
      chip, bot_to = map(int, re.findall('\d+', line))
      bot[bot_to].append(chip)
    else:
      bot_from, dest1, dest2 = map(int, re.findall('\d+', line))
      t1, t2 = re.findall(' (bot|output)', line)
      commands[bot_from] = (t1, dest1), (t2, dest2)

  while bot:
    for key, value in dict(bot).items():
      if len(value) != 2: continue
      v1, v2 = sorted(bot.pop(key))
      (t1, dest1), (t2, dest2) = commands[key]
      eval(f'{t1}[dest1].append(v1)')
      eval(f'{t2}[dest2].append(v2)')
      if v1 == 17 and v2 == 61: part1 = key

  part2 = math.prod(output[i][0] for i in range(3))
  return part1, part2


start = pfc()
part1, part2 = solve()
print('Part 1:', part1)
print('Part 2:', part2)
print(pfc() - start)
