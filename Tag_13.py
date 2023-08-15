from time import perf_counter as pfc


def is_wall(x, y):
  value = x * x + 3 * x + 2 * x * y + y + y * y + 1350
  return bin(value).count('1') % 2


def bfs():
  seen = {(1, 1)}
  steps = 0
  new_locations = seen

  part1 = part2 = None
  while not part1 or not part2:
    old_locations = new_locations.copy()
    new_locations = set()
    
    for x1,y1 in old_locations:
      for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        pos2 = x2,y2 = x1+dx, y1+dy
        if x2 < 0 or y2 < 0 or is_wall(*pos2) or pos2 in seen: continue
        seen.add(pos2)
        new_locations.add(pos2)
    
    steps += 1
    if (31, 39) in new_locations: part1 = steps
    if steps == 50: part2 = len(seen)
  
  return part1, part2  

start = pfc()
part1, part2 = bfs()

print(f'Part1: {part1}')
print(f'Part2: {part2}')
print(f'Ermittelt in {pfc() - start:.5f} Sek.')
