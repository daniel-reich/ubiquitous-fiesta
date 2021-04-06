
from itertools import product
def dice_roll(n, outcome):
    return sum(1 for t in product(range(1,7), repeat=n) if sum(t)==outcome)

