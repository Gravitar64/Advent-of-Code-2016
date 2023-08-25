from time import perf_counter as t1
import math
  
  
def solve(elves):
  part1 = int(bin(elves)[3:]+'1',2)
  part2 = elves - 3**int(math.log(elves,3))
  return part1, part2
    

start = t1() 
part1, part2 = solve(3004953)   
print(f'Part1 = {part1}')
print(f'Part2 = {part2}')
print(f'Ermittelt in {t1() - start:.5f} Sek.')