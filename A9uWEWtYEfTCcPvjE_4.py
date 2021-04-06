
from collections import defaultdict
def price_importance_sort(dct, b):
    prices = defaultdict(list)
    for i,x in dct.items():
        prices[x['price']].append(i)
    p = sorted(list(prices.keys()))
    a  = [p[0]] + p
    for x in prices:
        prices[x] = sorted(prices[x], key=lambda x: dct[x]['importance'])
    start = -1
    for x in range(len(p)-1, -1, -1):
        if p[x] <= b:
            start = x-1
            break
    out = []
    for x in range(max(start, 0)+1):
        for _ in range(2):
            if p[x] <= b and prices[p[x]]:
                out.append(prices[p[x]].pop())
                b -= p[x]
    return sorted(out)

