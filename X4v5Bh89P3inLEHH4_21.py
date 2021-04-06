
def spin_around(lst):
  a, b = lst.count('right') * 90, lst.count('left') * 90
  if len(lst) <= 1:
    return 0
  
  return (max(a, b) - min(a, b)) / 360

