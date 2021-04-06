
def is_legitimate(lst):
  return sum(lst[0] + [x[0]+x[-1] for x in lst[1:-1]] + lst[-1]) == 0

