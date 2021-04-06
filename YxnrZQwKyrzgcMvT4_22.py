
def rotate_transform(l, n):
  p = 2*(n>0)-1
  while n != 0:
    l = [list(x)[::-p] for x in zip(*l)][::p]
    n -= p
  return l

