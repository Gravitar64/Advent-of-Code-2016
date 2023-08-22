from time import perf_counter as t1
import hashlib


def solve(passcode):
  directions = {(0,-1):'U', (0,1):'D', (-1,0):'L', (1,0):'R'} 
  zu_besuchen = [(passcode, (0,0), '')]
  
  while zu_besuchen:
    pc, (x,y), pfad = zu_besuchen.pop(0)
    md5 = hashlib.md5(pc.encode()).hexdigest()[:4]
    for c,(dx,dy) in zip(md5,directions):
      if c not in 'bcdef': continue
      pos2 = x2, y2 = x+dx, y+dy
      if not -1 < x2 < 4 or not -1 < y2 < 4: continue
      d = directions[(dx,dy)]
      if pos2 == (3,3): 
        yield pfad+d
      else:
        zu_besuchen.append((pc+d, pos2, pfad+d))
      

start = t1()    
pfade = list(solve('rrrbmfta'))
print(f'Part1 = {pfade[0]}')
print(f'Part2 = {len(pfade[-1])}')
print(f'Ermittelt in {t1() - start:.5f} Sek.')