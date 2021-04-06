
from itertools import permutations
def discount(n, txt):
    if not txt:
        return n
    min_price = n
    for permutation in permutations(txt.split(', ')):
        price = n
        for str_discount in permutation:
            if str_discount[-1] == '%':
                price -= price * float(str_discount[:-1]) / 100
            else:
                price -= float(str_discount)
        if price < min_price:
            min_price = price
    return round(min_price, 2)

