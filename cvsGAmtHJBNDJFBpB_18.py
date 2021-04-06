
def can_traverse(x):
   lst = list(zip(*x))
   return all(abs(x.count(0) - y.count(0)) <= 1 for x, y in zip(lst, lst[1:]))

