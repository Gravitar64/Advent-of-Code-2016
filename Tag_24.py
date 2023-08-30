from time import perf_counter as pfc
import itertools


def load(file):
  with open(file) as f:
    return f.readlines()


#generates shortest distance between every possible number-pair and returns
#a dictionary key = a,b: value = shortest distance between a,b
def bfs(p):
  opens = {(x,y) for y,z in enumerate(p) for x,c in enumerate(z) if c != '#'}
  numbrs = {p[y][x]:(x,y) for x,y in opens if p[y][x].isdigit()}
  distances = {}
  
  for a,b in itertools.combinations(numbrs,2):
    (x,y), target = numbrs[a], numbrs[b]
    queue, seen = [(x,y,0)], set()
    while queue:
      x,y,steps = queue.pop(0)
      if (x,y) == target: 
        distances[a,b] = steps
        distances[b,a] = steps
        break
      for dx,dy in ((1,0), (-1,0), (0,1), (0,-1)):
        x1,y1 = x+dx, y+dy
        if (x1,y1) in seen or not (x1,y1) in opens: continue
        seen.add((x1,y1))
        queue.append((x1,y1,steps+1))
  return distances      
  

def solve(p,part1):
  distances = bfs(p)
  
  best = 99999999
  for path in itertools.permutations('1234567'):
    path = ('0',)+path if part1 else ('0',)+path+('0',)
    best = min(best, sum(distances[a,b] for a,b in itertools.pairwise(path)))
  return best 
           
   
start = pfc()
puzzle = load('Tag_24.txt')
print('Part 1:', solve(puzzle, True))
print('Part 2:', solve(puzzle, False))
print(pfc() - start)


