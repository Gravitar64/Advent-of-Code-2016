from time import perf_counter as pfc
import re


def load(file):
  with open(file) as f:
    return [x.strip() for x in f]


def is_abba(e):
  return re.search(r'(.)(?!\1)(.)\2\1', e) != None


def has_tls(e):
  for md in re.finditer(r'\[.*?\]', e):
    if is_abba(md.group(0)):
      return False
  return is_abba(e)


def solve(p):
  return sum(map(has_tls, p))


puzzle = load('Tag_07.txt')

start = pfc()
print(solve(puzzle), pfc() - start)
