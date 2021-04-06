
def almost_sorted(lst):
  if lst == sorted(lst) or lst == sorted(lst,reverse=True): return False
  c = -1
  while True:
    c += 1
    x = [a for a in lst]
    if c==len(x):
      return False
    x.pop(c)
    if x == sorted(x) or x == sorted(x,reverse=True):
      return True

