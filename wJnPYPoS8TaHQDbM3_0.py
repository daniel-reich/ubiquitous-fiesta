
from itertools import product
​
def dice_roll(n, outcome):
    return sum(sum(p) == outcome for p in product(range(1, 7), repeat=n))

