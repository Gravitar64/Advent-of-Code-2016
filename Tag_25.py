from time import perf_counter as pfc


class Computer():
  def __init__(self,p):
    self.p = p
    self.l = len(p)
    self.pc = 0
    self.cycle = 0
    self.clock = ''
    self.register = dict(a=0, b=0, c=0, d=0)
    
  def run(self):
    while self.cycle < 40000:
      self.execute(self.p[self.pc])
    return self.clock
  
  def execute(self,command):
    if len(command) == 2:
      m,v1 = command
    else:
      m,v1,v2 = command  
    match m:
      case 'inc': self.register[v1] += 1
      case 'dec': self.register[v1] -= 1
      case 'cpy': self.register[v2] = self.read(v1)
      case 'jnz': self.pc += 1 if not self.read(v1) else self.read(v2)
      case 'out': self.clock += str(self.read(v1))
    if m != 'jnz': self.pc += 1
    self.cycle += 1
     
      
  def read(self,v):
    return self.register[v] if v in self.register else int(v)     


def load(file):
  with open(file) as f:
    return [line.strip().split() for line in f]


def solve(p):
  for i in range(200):
    cmp = Computer(p)
    cmp.register['a'] = i
    clock = cmp.run()
    if clock.startswith('010101010101'):
      return i
    
start = pfc()
puzzle = load('Tag_25.txt')
print('Part 1:', solve(puzzle))
print(pfc() - start)