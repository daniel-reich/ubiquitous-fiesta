
def product(lst):
  a = sorted(set(lst))
  return a[-1] * a[-2] if len(a)>1 else a[0] * a[0]

