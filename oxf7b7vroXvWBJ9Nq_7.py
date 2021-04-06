
def discount(n, s):
  if not len(s): return n
  by_percent = lambda p: 1 if not '%' in p else -1 if '%' in p else 0
  for x in sorted(s.split(', '), key=by_percent):
    n -= n/100*float(x[:-1]) if '%' in x else float(x)
  return round(n, 2)

