
def discount(n, txt):
  if not txt:
    return n
  discounts = txt.split(', ')
  percents = [float(x[:-1]) / 100 for x in discounts if '%' in x]
  fixed = [float(x) for x in discounts if '%' not in x]
  for x in percents:
    n -= n * x
  for x in fixed:
    n -= x
  return round(n, 2)

