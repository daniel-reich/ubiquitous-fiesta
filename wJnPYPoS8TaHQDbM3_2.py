
def dice_roll(n, target):
    '''
    Returns the number of ways that the sum of n dice rolled together can add
    up to target
    '''
    from itertools import combinations
​
    return sum(sum(combo) == target for combo
           in set(list(combinations(list(range(1,7)) * n ,n))))

