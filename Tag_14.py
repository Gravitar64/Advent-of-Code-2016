from time import perf_counter as t1
import hashlib
import re
import functools


@functools.lru_cache(maxsize=None)
def get_hash(s,part1):
  hash = hashlib.md5(s.encode()).hexdigest()
  if part1: return hash
  for _ in range(2016):
    hash = hashlib.md5(hash.encode()).hexdigest()
  return hash  


def solve(part1):
  salt, keys, i = 'jlmsuwbz', 0, 0
    
  while True:
    hash = get_hash(f'{salt}{i}', part1)
    match = re.search(r'(\w)\1\1', hash)
    if not match: 
      i += 1
      continue    
    
    quintett = match.group(0)[0]*5
    for i2 in range(i+1,i+1000):
      hash2 = get_hash(f'{salt}{i2}', part1)
      if not re.search(quintett, hash2): continue
      keys += 1
      break
    
    if keys == 64: return i
    i += 1
    
  
start = t1()
print(f'Part1: Index = {solve(True)} for 64th key')
print(f'Part2: Index = {solve(False)} for 64th key')
print(f'Ermittelt in {t1() - start:.5f} Sek.')