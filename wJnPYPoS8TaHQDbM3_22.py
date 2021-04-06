
import itertools
def dice_roll(n, outcome):
  dice = [[1,2,3,4,5,6]]*n
  return sum(1 for i in itertools.product(*dice) if sum(i) == outcome)

