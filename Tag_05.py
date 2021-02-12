from time import perf_counter as pfc
import hashlib


def solve(p):
  part1, part2 = '', {}
  for n in range(100_000_000):
    hash = hashlib.md5(p+str(n).encode()).hexdigest()
    if hash[:5] == '00000':
      pos, val = hash[5:7]
      if len(part1) < 8:
        part1 += pos
      if pos < '8' and pos not in part2:   
        part2[pos] = val
        if len(part2) == 8:
          return part1, ''.join(v for _,v in sorted(part2.items()))

puzzle = 'uqwqemis'.encode()

start = pfc()
print(solve(puzzle), pfc() - start)
