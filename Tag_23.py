from time import perf_counter as pfc
from copy import deepcopy
import math


class Computer():
  def __init__(self,p):
    self.p = deepcopy(p)
    self.l = len(p)
    self.pc = 0
    self.register = dict(a=0, b=0, c=0, d=0)
    
  def run(self):
    while self.pc < self.l:
      self.execute(self.p[self.pc])
    return self.register['a']  
  
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
      case 'tgl': 
        pc2 = self.pc+self.register[v1]
        if pc2 < self.l: 
          command2 = self.p[pc2]
          if len(command2) == 2:
            command2[0] = 'dec' if command2[0] == 'inc' else 'inc'
          else:
            command2[0] = 'cpy' if command2[0] == 'jnz' else 'jnz'
    if m != 'jnz': self.pc += 1 
      
  def read(self,v):
    return self.register[v] if v in self.register else int(v)     


def load(file):
  with open(file) as f:
    return [line.strip().split() for line in f]


def solve(p,s):
  cmp = Computer(p)
  cmp.register['a'] = s
  return cmp.run()

    
start = pfc()
puzzle = load('Tag_23.txt')

print('Part 1:', solve(puzzle,7))
print('Part 2:', 73*91+math.factorial(12))

print(pfc() - start)