
def discount(n, txt):
  if not txt:
    return n
​
  discounts = sorted(txt.split(', '), key=str.isdigit)
  for d in discounts:
    if '%' in d:
      n *= 1 - float(d[:-1])/100
    else:
      n -= float(d)
  return round(n,2)

