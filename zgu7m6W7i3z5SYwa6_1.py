
def is_equal(lst):
  f = lambda i: sum(int(x) for x in str(lst[i]))
  return f(0) == f(1)

