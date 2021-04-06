
from itertools import combinations
def price_importance_sort(dct, b):
  best = ([], b+1, 0)
  for n in range(1, len(dct)):
    for comb in combinations(dct, n):
      cost = sum(dct[i]['price'] for i in comb)
      if cost <= b:
        imp = sum(dct[i]['importance'] for i in comb)
        if imp > best[2] or (imp == best[2] and cost < best[1]):
          best = (comb, cost, imp)
  return sorted(best[0])

