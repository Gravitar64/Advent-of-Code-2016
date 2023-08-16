from time import perf_counter as t1
import re


def load_file(file):
  with open(file) as f:
    return [tuple(map(int,re.findall('\d+',l))) for l in f.readlines()]
    

def solve(p, part2=False):
  if part2: p.append((1,11,0,0))
  act_time = 0
  while True:
    for i, (_, positions, _, position) in enumerate(p,start=1):
      if not (position+act_time+i) % positions: continue
      break
    else:
      return act_time
    act_time += 1    
        

  
start = t1()
puzzle = load_file('Tag_15.txt')
print(f'Part1: {solve(puzzle)}')
print(f'Part2: {solve(puzzle, True)}')
print(f'Ermittelt in {t1() - start:.5f} Sek.')