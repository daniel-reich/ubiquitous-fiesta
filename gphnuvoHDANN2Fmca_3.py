
def odd_sort(lst):
  odds = sorted([x for x in lst if x%2 != 0])
  evensplace = [(lst[x], x) for x in range(len(lst)) if lst[x]%2 == 0]
  for x in evensplace:
    odds.insert(x[1],x[0])
  return odds

