from time import perf_counter as pfc 

def load(file):
  with open(file) as f:
    return [(e[0], int(e[1:])) for z in f for e in z.split(', ')]

def solve(puzzle):
  pos, pos2, rcht, sol2 = [0,0], [0,0], [0,-1], None
  visit = set()
  for rot, anz in puzzle:
    x,y = rcht
    rcht = [-y,x] if rot == 'R' else [y,-x]
    pos = [a+b*anz for a,b in zip(pos,rcht)]
    for _ in range(anz):
      pos2 = tuple(a+b for a,b in zip(pos2,rcht))
      if not sol2 and pos2 in visit: sol2 = pos2
      visit.add(pos2)  
  return sum([abs(a) for a in pos]), sum([abs(a) for a in sol2])   

puzzle = load('Tag_01.txt')

start = pfc()
print(solve(puzzle), pfc() - start)