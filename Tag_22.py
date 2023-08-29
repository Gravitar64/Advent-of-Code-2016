from time import perf_counter as t1
import re


def load(file):
  with open(file) as f:
    return [tuple(map(int,re.findall('\d+', z))) for z in f]


def solve(p):
  part1 = 0
  for x,y,_,used,_,_ in p:
    if not used: continue
    for x1,y1,_,_,avail,_ in p:
      part1 += used <= avail and (x,y) != (x1,y1)
  return part1    


def solve2(p,target): #bfs from "hole" to target + (x-Pos-1) * 5
  x,y,size = [(x,y,size) for x,y,size,used,*args in p if used == 0][0]
  queue, visited = [(x,y,0)], set((x,y))
  spaces = {(x,y) for x,y,_,used,*args in p if used <= size} 
  
  while queue:
    x,y,steps = queue.pop(0)
    if (x,y) == target: break
    for dx,dy in ((0,1),(1,0),(-1,0),(0,-1)):
      x1,y1 = x+dx, y+dy
      if (x1,y1) in visited or not (x1,y1) in spaces: continue
      visited.add((x1,y1))
      queue.append((x1,y1,steps+1))
  return steps+5*(target[0]-1)    
      

start = t1()
puzzle = load('Tag_22.txt')
print(f'Part1 = {solve(puzzle)}')
print(f'Part1 = {solve2(puzzle,(36,0))}')
print(f'Ermittelt in {t1() - start:.5f} Sek.')
