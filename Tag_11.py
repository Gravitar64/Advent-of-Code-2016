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
    priority, (elevator, floors) = heapq.heappop(queue)
    if elevator == 3 and all(not x for x in floors[:-1]): 
      return results[(elevator, floors)]
    next_elevators = [dir + elevator for dir in [-1,1] if -1 < dir+elevator < 4]
    moves = list(combinations(floors[elevator], 2)) + list(combinations(floors[elevator], 1))
    for move in moves:
      for next_elevator in next_elevators:
        new_floors = list(floors)
        new_floors[elevator] = tuple(x for x in new_floors[elevator] if x not in move)
        new_floors[next_elevator] = tuple(new_floors[next_elevator] + move)
        if not check(new_floors[elevator]) or not check(new_floors[next_elevator]): continue
        next_p = sort_floors((next_elevator, tuple(new_floors)))
        steps = results[((elevator, floors))] + 1
        if next_p not in results or steps < results[next_p]:
          results[next_p] = steps
          priority = steps  - len(new_floors[3])*10
          heapq.heappush(queue, (priority, next_p))
          


start = pfc()
po, th, pr, ru, co, el, di = 1, 2, 3, 4, 5, 6, 7
part1 = (0, ((po, th, -th, pr, ru, -ru, co, -co), (-po, -pr), (), ()))
part2 = (0, ((po, th, -th, pr, ru, -ru, co, -co,
         el, -el, di, -di), (-po, -pr), (), ()))


print('Part 1:', solve(sort_floors(part1)))
print('Part 2:', solve(sort_floors(part2)))
print(pfc() - start)
