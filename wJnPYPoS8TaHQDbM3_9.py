
from itertools import product
def dice_roll(n, outcome):
  return 1 if n==1 else sum([1 for item in list(product(*[[1,2,3,4,5,6] for i in range(n)])) if sum(item)==outcome])

