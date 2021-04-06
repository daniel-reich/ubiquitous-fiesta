
from collections import Counter
import itertools as it
​
def dice_roll(n, outcome):
    exec('combos = list(it.product({}))'.format((n*'{},'.format(Counter(range(1, 7))))[:-1]), globals())
    return sum([1 if outcome == sum(list(combo)) else 0 for combo in combos])

