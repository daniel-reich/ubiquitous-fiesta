
def spin_around(lst):
  r = lst.count('right')
  l = lst.count('left')
  return abs((r*90 - l*90))//360

