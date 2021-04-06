
def dice_roll(n, outcome):
  from itertools import product
  from functools import reduce
  dice = [i for i in range(1,6+1)]
  dices = [dice for i in range(n)]
  possibilities = product(*dices)
  possibilities = list(map(lambda x: reduce(lambda a, b: a+b, x), possibilities))
  return possibilities.count(outcome)

