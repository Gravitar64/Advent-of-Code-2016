from time import perf_counter as t1
import re


def load(file):
  with open(file) as f:
    return sorted([tuple(map(int, re.findall('\d+', z))) for z in f])


def solve(p,part1):
  lowest = ips = 0
  for low,high in p:
    if low > lowest:
      if part1: return lowest
      ips += low - lowest  
    if lowest <= high: lowest = high+1
  return ips  


start = t1()
puzzle = load('Tag_20.txt')

print(f'Part1 = {solve(puzzle, True)}')
print(f'Part2 = {solve(puzzle, False)}')
print(f'Ermittelt in {t1() - start:.5f} Sek.')
