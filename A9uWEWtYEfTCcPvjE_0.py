
def price_importance_sort(dct, b):
  opps = {tuple():[0,0]}
  for item in dct:
    for comb in list(opps.keys())[:]:
      if opps[comb][0] + dct[item]['price'] <= b:
        opps[comb+(item,)] = [opps[comb][0] + dct[item]['price'], \
                           opps[comb][1] + dct[item]['importance']]
  return sorted(max(opps, key = lambda op: opps[op][1]))

