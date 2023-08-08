from time import perf_counter as pfc
import re
import numpy as np


def load(file):
  with open(file) as f:
    return [x.strip() for x in f]


def solve(p):
  for zeile in p:
    a, b = map(int, re.findall('\d+', zeile))
    if zeile[:2] == 're':
      grid[:b, :a] = 1
    else:
      rotate_row(a,b) if zeile[7] == 'r' else rotate_col(a,b)
  return np.sum(grid)


def rotate_row(row, n):
  grid[row] = np.roll(grid[row],n)


def rotate_col(col, n):
  grid[ :,col] = np.roll(grid[ :,col],n)
  

puzzle = load('Tag_08.txt')
width, height = 50,6
grid = np.zeros((height,width))
#[[0]*width for _ in range(height)]

start = pfc()
print(solve(puzzle), pfc() - start)
for z in grid:
  print(''.join(['*' if n == 1 else ' ' for n in z]))
