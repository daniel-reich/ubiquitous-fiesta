
from itertools import combinations
​
def dice_roll(n, outcome):
    
    dices = [1, 2, 3, 4, 5, 6] * n
​
    variations = []
    for i in combinations(dices, n):
        variations.append(i)
​
    variations = list(set(variations))
​
    comb = []
    for i in variations:
        comb.append(sum(i))
​
    return comb.count(outcome)

