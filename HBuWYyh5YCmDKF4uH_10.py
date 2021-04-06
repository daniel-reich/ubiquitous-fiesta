
is_sorted = lambda l: l == sorted(l) or l[::-1] == sorted(l)
​
def almost_sorted(l):
​
  if is_sorted(l):
    return False
  
  for i in range(len(l)):
    fl = l.copy()
    fl.pop(i)
    if is_sorted(fl):
      return True
​
  return False

