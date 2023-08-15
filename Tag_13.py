from time import perf_counter as t1


def is_wall(x, y):
  value = x * x + 3 * x + 2 * x * y + y + y * y + 1350
  return bin(value).count('1') % 2


def bfs(start, end):
  queue, seen = [(*start, 0)], set()
  while True:
    x, y, steps = queue.pop(0)

    if (x, y) == end: return steps, part2
    if steps == 50: part2 = len(seen)

    seen.add((x, y))
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
      pos2 = x2, y2 = x+dx, y+dy
      if x2 < 0 or y2 < 0 or is_wall(*pos2) or pos2 in seen: continue
      queue.append((x2, y2, steps+1))


start = t1()
part1, part2 = bfs((1, 1), (31, 39))

print(f'Part1: {part1} Steps')
print(f'Part2: {part2} Locations')
print(f'Ermittelt in {t1() - start:.5f} Sek.')
