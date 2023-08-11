from time import perf_counter as pfc

class Computer():
  def __init__(self):
    self.pc = 0
    self.register = dict(a=0, b=0, c=0, d=0)
    
  def execute(self,command):
    if len(command) == 2:
      m,v1 = command
    else:
      m,v1,v2 = command  
    match m:
      case 'inc': self.register[v1] += 1
      case 'dec': self.register[v1] -= 1
      case 'cpy': self.register[v2] = self.read(v1)
      case 'jnz': self.pc += 1 if not self.read(v1) else int(v2)               
    if m != 'jnz': self.pc += 1 
      
  def read(self,v):
    return self.register[v] if v in self.register else int(v)     


def load(file):
  with open(file) as f:
    return [line.strip().split() for line in f]


def solve(p,part2):
  cmp = Computer()
  if part2: cmp.register['c'] = 1
  while cmp.pc < len(p):
    cmp.execute(p[cmp.pc])
  return cmp.register['a']  

    
start = pfc()
puzzle = load('Tag_12.txt')

print('Part 1:', solve(puzzle, False))
print('Part 2:', solve(puzzle, True))

print(pfc() - start)