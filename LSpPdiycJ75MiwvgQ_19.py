
def fac(n):
  return 1 if n<2 else n*fac(n-1)
def grid_pos(lst):
  return fac(sum(lst))//(fac(lst[0])*fac(lst[1]))

