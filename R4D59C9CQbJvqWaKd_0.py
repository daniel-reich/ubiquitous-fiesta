
def batting_avg(lst):
  a, b = map(sum, zip(*lst))
  return '{:.3f}'.format(a/b)[1:]

