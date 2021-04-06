
from itertools import product
​
def dice_roll(n, outcome):
  return sum(sum(x) == outcome for x in product(*[range(1, 7)] * n))

