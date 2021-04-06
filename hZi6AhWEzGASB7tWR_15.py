
def check(lst):
  a = [y-x for x, y in zip(lst[:-1], lst[1:])]
  d = all(x < 0 for x in a)
  return 'increasing' if min(a) > 0 else 'decreasing' if d else 'neither'

