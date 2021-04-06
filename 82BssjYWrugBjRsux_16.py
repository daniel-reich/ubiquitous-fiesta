
def index_multiplier(lst):
  s = 0
  lst2 = []
  for i in lst:
    i = i * s
    lst2.append(i)
    s += 1
  return sum(lst2)

