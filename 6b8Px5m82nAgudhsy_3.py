
from itertools import permutations
​
def next_number(num):
  digits = [c for c in ('%d' % num)]
  n = len(digits)
​
  permuted = set()
  for t in permutations(digits, n):
    permuted.add(int(''.join(t)))
​
  permuted = sorted(permuted)
  assert(num in permuted)
  index = permuted.index(num)
  if index == len(permuted)-1: return num
  else: return permuted[index+1]

