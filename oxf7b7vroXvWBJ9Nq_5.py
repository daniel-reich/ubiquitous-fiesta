
def discount(cost, discounts):
    '''
    Returns price after discounts applied to cost so as to maximise the
    discounts as per the instructions
    '''
    from itertools import permutations
    from functools import reduce
​
    if len(discounts) == 0:
        return round(cost, 2)
    
    uniques = set()
    best = cost
    discounts = discounts.split(', ')
    
​
    for combo in permutations(discounts, len(discounts)):
        if combo not in uniques:
            comb_list = [cost] + list(combo)
            price = reduce(lambda a,b: a - float(b) if b[-1] != '%' else \
                           a - float(b[:-1])/100 * a, comb_list)
            uniques.add(combo)
            if price < best:
                best = price
​
    return round(best, 2)

