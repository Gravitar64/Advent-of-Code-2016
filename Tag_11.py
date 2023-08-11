from time import perf_counter as pfc
import heapq
from itertools import combinations


def sort_floors(p):
  e = []
  for floor in p[1]:
    e.append(tuple(sorted(floor)))
  return (p[0], tuple(e))
  
  
def check(floor):
  if (not floor) or max(floor) < 0: return True
  return all(-item in floor for item in floor if item < 0)  


def solve(p):
  queue = []
  heapq.heappush(queue, (0, p))
  results = {p: 0}
  while queue:
    prio, (elev1, floors) = heapq.heappop(queue)
    if elev1 == 3 and all(not x for x in floors[:-1]): return results[(elev1, floors)]
    
    next_elevators = [dir + elev1 for dir in [-1,1] if -1 < dir+elev1 < 4]
    moves = list(combinations(floors[elev1], 2)) + list(combinations(floors[elev1], 1))
    
    for move in moves:
      for elev2 in next_elevators:
        new = list(floors)
        new[elev1] = tuple(x for x in new[elev1] if x not in move)
        new[elev2] = tuple(new[elev2] + move)
        if not check(new[elev1]) or not check(new[elev2]): continue
        
        next_p = sort_floors((elev2, tuple(new)))
        steps = results[((elev1, floors))] + 1
        
        if next_p not in results or steps < results[next_p]:
          results[next_p] = steps
          prio = steps  - len(new[3])*10
          heapq.heappush(queue, (prio, next_p))
          

start = pfc()
po, th, pr, ru, co, el, di = 1, 2, 3, 4, 5, 6, 7
part1 = (0, ((po, th, -th, pr, ru, -ru, co, -co), (-po, -pr), (), ()))
part2 = (0, ((po, th, -th, pr, ru, -ru, co, -co,
         el, -el, di, -di), (-po, -pr), (), ()))


print('Part 1:', solve(sort_floors(part1)))
print('Part 2:', solve(sort_floors(part2)))
print(pfc() - start)