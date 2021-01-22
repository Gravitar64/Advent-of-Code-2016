from time import perf_counter as pfc 

def load(file):
  with open(file) as f:
    return [z.strip() for z in f]

def solve(puzzle, part1=True):
  pos = (1,1) if part1 else (0,2)
  dirs = dict(U=(0,-1), D=(0,1), L=(-1,0), R=(1,0))
  if part1:
    keypad = {(x,y):str(y*3+x+1) for x in range(3) for y in range(3)}
  else:
    keypad = {(2,0):'1', (1,1):'2', (2,1):'3', (3,1):'4',
              (0,2):'5', (1,2):'6', (2,2):'7', (3,2):'8', (4,2):'9',
              (1,3):'A', (2,3):'B', (3,3):'C', (2,4):'D'}  
  code = ''
  for zeile in puzzle:
    for c in zeile:
      if (pos2 := tuple(a+b for a,b in zip(dirs[c], pos))) in keypad:
        pos = pos2
    code += keypad[pos]  
  return code

puzzle = load('Tag_02.txt')

start = pfc()
print(solve(puzzle), pfc() - start)

start = pfc()
print(solve(puzzle, False), pfc() - start)