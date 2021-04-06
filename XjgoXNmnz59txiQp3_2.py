
from itertools import product
​
def split(number):
  if number == 1: return 1
  out = []
  for twos, threes in product(range(5), range(10)):
    if 3*threes + 2*twos == number:
      out.append(3**threes * 2**twos)
  return max(out)

