from time import perf_counter as t1


def dragon_curve(a,l):
  while len(a) < l:
    b = ''.join('0' if c=='1' else '1' for c in reversed(a))
    a = a + '0' + b
  return a[:l]


def checksum(a):
  while True:
    l = []
    for b1, b2 in zip(a[::2], a[1::2]):
      l.append('1') if b1==b2 else l.append('0')
    if len(l) % 2: return ''.join(l)
    a = l.copy()
    

def solve(a,l):
  a = dragon_curve(a,l)
  return checksum(a) 
  
  
start = t1()
print(f'Part1 = {solve("11110010111001001", 272)}')
print(f'Part2 = {solve("11110010111001001", 35651584)}')
print(f'Ermittelt in {t1() - start:.5f} Sek.')