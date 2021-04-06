
def min_swaps(string):
  a,b = map(string[::2].count, ['0','1'])
  x,y = map(string[1::2].count, ['0','1'])
  return min(a+y, b+x)

