from time import perf_counter as pfc
import re
import itertools
import numpy as np


def load(file):
  with open(file) as f:
    return [x.strip() for x in f]


def solve(p):
  for zeile in p:
    a, b = map(int, re.findall('\d+', zeile))
    if zeile[:2] == 're':
      rect(a, b)
    else:
      rotate_row(a,b) if zeile[7] == 'r' else rotate_col(a,b)
  return sum(sum(z) for z in grid)


def rotate_row(row, n):
  r = grid[row]
  grid[row] = r[-n:]+r[:width-n]


def rotate_col(col, n):
  c = [grid[y][col] for y in range(6)]
  c = c[-n:]+c[:height-n]
  for y, value in enumerate(c):
    grid[y][col] = value


def rect(a, b):
  for x,y in itertools.product(range(a), range(b)):
    grid[y][x] = 1


puzzle = load('Tag_08.txt')
width, height = 50,6
grid = [[0]*width for _ in range(height)]

start = pfc()
print(solve(puzzle), pfc() - start)
for z in grid:
  print(''.join(['*' if n == 1 else ' ' for n in z]))
