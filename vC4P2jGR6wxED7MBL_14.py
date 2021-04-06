
def larger_than_right(lst):
  m = []
  [m.append(y) for x,y in enumerate(lst) if max(lst[x:])==y and y not in m]
  return m

