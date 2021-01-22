from time import perf_counter as pfc 

def load(file):
  with open(file) as f:
    return [[int(l) for l in t.split()] for t in f]
    
def is_valid(triangle):
  a,b,c = sorted(triangle)
  return a+b > c

def solve(p):
  part1 = sum([is_valid(triangle) for triangle in p])
  p, l = [list(t) for t in zip(*p)], len(p)
  return part1, sum([is_valid(col[i:i+3]) for col in p for i in range(0,l,3)])

puzzle = load('Tag_03.txt')

start = pfc()
print(solve(puzzle), pfc() - start)
