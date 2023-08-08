from time import perf_counter as pfc
import re
import numpy as np


def load(file):
  with open(file) as f:
    return f.readlines()

start = pfc()
grid = np.zeros((6,50),dtype=int)
puzzle = load('Tag_08.txt')

for zeile in puzzle:
  a, b = map(int, re.findall('\d+', zeile))
  if zeile[:2] == 're': grid[:b, :a] = 1
  elif zeile[7] == 'r': grid[a] = np.roll(grid[a],b)
  else:                 grid[:,a] = np.roll(grid[:,a],b)
    
print(f'Part 1: {np.sum(grid)} in {pfc()-start} Sek.')
for z in grid:
  print(''.join(['▓' if n == 1 else ' ' for n in z]))
