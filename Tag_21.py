from time import perf_counter as t1
import itertools


def load(file):
  with open(file) as f:
    return [z.strip().split() for z in f]


def swapletter(s, a, b):
  i1, i2 = s.index(a), s.index(b)
  swapposition(s, i1, i2)


def swapposition(s, a, b):
  s[a], s[b] = s[b], s[a]


def reverse(s, a, b):
  s[a:b+1] = reversed(s[a:b+1])


def move(s, a, b):
  p = s.pop(a)
  s.insert(b, p)


def rotateleft(s, a):
  return s[a:]+s[:a]


def rotateright(s, a):
  return s[-a:]+s[:-a]


def rotatebased(s, a):
  i = s.index(a)
  i = (i + 2 if i >= 4 else i + 1) % 8
  return s[-i:]+s[:-i]


def solve(p, start):
  for w1, w2, *a in p:
    if w1+w2    == 'swapletter': swapletter(start, a[0], a[-1])
    elif w1+w2  == 'swapposition': swapposition(start, int(a[0]), int(a[-1]))
    elif w1     == 'move': move(start,int(a[0]), int(a[-1]))
    elif w1+w2  == 'rotatebased': start = rotatebased(start, a[4])
    elif w1     == 'reverse': reverse(start, int(a[0]), int(a[-1]))
    elif w1+w2  == 'rotateright': start = rotateright(start, int(a[0]))
    elif w1+w2  == 'rotateleft':  start = rotateleft(start, int(a[0]))
  return ''.join(start)


start = t1()
puzzle = load('Tag_21.txt')

print(f'Part1 = {solve(puzzle, list("abcdefgh"))}')
for s in itertools.permutations("abcdefgh"):
  if solve(puzzle, list(s)) != "fbgdceah": continue
  print(f'Part2 = {"".join(s)}')
  break
print(f'Ermittelt in {t1() - start:.5f} Sek.')
