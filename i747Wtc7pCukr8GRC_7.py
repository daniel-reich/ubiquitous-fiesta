
def max_product(lst):
    prod = -99999999999999999999
​
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                prod = max(prod, lst[i] * lst[j] * lst[k])
    return prod
​
​
def min_product(lst):
    prod = 99999999999999999999
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                prod = min(prod, lst[i] * lst[j] * lst[k])
    return prod

