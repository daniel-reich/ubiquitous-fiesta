
def discount(n, txt):
  discounts = txt.split(', ')
  for d in discounts:
    if '%' in d:
      n *= (1 - float(d.strip('%')) / 100)
  return round(n - sum([float(d) for d in discounts if d and '%' not in d]), 2)

