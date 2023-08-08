from time import perf_counter as pfc
import re


def load(file):
  with open(file) as f:
    return f.read()


def decompress(data, part2):
  answer = s1 = 0
  while s1 < len(data):
    if data[s1] == '(':
      s2 = data.index(')', s1)
      subs, times = map(int, re.findall('\d+', data[s1:s2]))
      answer += times * \
          decompress(data[s2+1:s2+1+subs], part2) if part2 else subs*times
      s1 = s2+subs
    else:
      answer += 1
    s1 += 1
  return answer


start = pfc()
puzzle = load('Tag_09.txt')
print(f'Answer #1: {decompress(puzzle, False)} in {pfc()-start} Sek.')
print(f'Answer #2: {decompress(puzzle, True)} in {pfc()-start} Sek.')
