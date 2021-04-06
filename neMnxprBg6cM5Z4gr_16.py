
def arithmetic_progression(start, diff, n):
  ap = []
  for i in range(n):
    ap.append(str(start))
    start += diff
  return ', '.join(ap)

