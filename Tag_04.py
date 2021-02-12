from time import perf_counter as pfc
from collections import Counter
import re


def load(file):
  with open(file) as f:
    return f.read()


def cipher(c, sector_ID):
  return chr(97+(ord(c)-97+sector_ID % 26) % 26)


def solve(p, part1=0):
  pattern = r'([a-z-]+)(\d+)\[(\w+)\]'
  for encrypted_name, sector_ID, checksum in re.findall(pattern, p):
    encrypted_name = encrypted_name.replace('-', '')
    sector_ID = int(sector_ID)
    tops = [(-n, c) for c, n in Counter(encrypted_name).most_common()]
    ranked = ''.join([c for n, c in sorted(tops)])
    if checksum == ranked[:5]:
      part1 += sector_ID
      decrypted_name = ''.join([cipher(c, sector_ID) for c in encrypted_name])
      if 'northpole' in decrypted_name: part2 = sector_ID
  return part1, part2


puzzle = load('Tag_04.txt')

start = pfc()
print(solve(puzzle), pfc() - start)
