from time import perf_counter as t1

  
def solve2(tiles,rows):
  row = ['^.'.find(c) for c in tiles]
  safe = sum(row)
  for i in range(1,rows):
    row = [1] + row + [1]
    row = [left == right for left, right in zip(row, row[2:])]
    safe += sum(row)
  return safe    
    

start = t1()    
puzzle = '...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^'
print(f'Part1 = {solve2(puzzle,40)}')
print(f'Part2 = {solve2(puzzle,400_000)}')
print(f'Ermittelt in {t1() - start:.2f} Sek.')