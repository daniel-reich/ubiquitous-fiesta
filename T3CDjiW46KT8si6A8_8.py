
def product(l):
  y = sorted(list(set(l)))
  return y[-1] * y[-2] if len(set(l)) > 1 else sorted(l)[-1] * sorted(l)[-2]

