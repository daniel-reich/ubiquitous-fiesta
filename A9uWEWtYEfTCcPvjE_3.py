
import itertools
​
def price_importance_sort(dct, b):
    top_importance = 0
    items = list(dct.items())
    #print(items)
    n = len(dct.keys())
    for k in range(1, n + 1):
        L = list(range(n))
        for comb in itertools.combinations(L, k):
            if sum([items[i][1]["price"] for i in comb]) <= b:
                imp = sum([items[i][1]["importance"] for i in comb])
                if imp > top_importance:
                    top_importance = imp
                    ans = [items[i][0] for i in comb] 
    return sorted(ans)

