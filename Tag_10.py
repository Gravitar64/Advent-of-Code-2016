from time import perf_counter as pfc
import re
from collections import defaultdict
import math


def load(file):
  with open(file) as f:
    return [(list(map(int,re.findall('\d+',line))), line.strip().split()) for line in f]


def solve():
  outputs, bots, commands = {}, defaultdict(list), {}
  bots_with_2 = [] 
  
  for numbers, command in load('Tag_10.txt'):
    if len(numbers) == 2:
      bots[numbers[1]].append(numbers[0])
      if len(bots[numbers[1]]) == 2: bots_with_2.append(numbers[1])
    else:
      commands[numbers[0]] = [(numbers[1], command[5]), (numbers[2], command[10])]
      
  while bots_with_2:
    for key,value in bots.items():
      if set((61,17)) == set(value): part1 = key
    for bot_from in bots_with_2:
      low_high = min(x for x in bots[bot_from]), max(x for x in bots[bot_from])
      bots[bot_from] = []
      for (bot_to, target), chip in zip(commands[bot_from], low_high):
        if target == 'bot':
          bots[bot_to].append(chip)
        else:
          outputs[bot_to] = chip
    bots_with_2 = [key for key,value in bots.items() if len(value) == 2]
  
  part2 = math.prod(outputs[i] for i in range(3))
  return part1, part2
    
  
            
      
      
    
      
  
      
 
start = pfc()
part1, part2 = solve()
print('Part 1:', part1)
print('Part 2:', part2 )
print(pfc() - start)
