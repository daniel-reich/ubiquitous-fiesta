
def order(lst):
  arr = sorted([(x,y) for x,y in zip(lst, list(range(len(lst))))])
  return [a[1] for a in arr]

