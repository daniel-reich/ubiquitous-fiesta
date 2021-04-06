
def is_polygonal(n):
  if n == 1: return '0th of all'
  K = []
  for i in range(n, 0, -1):
    k = round(2 / i / (i + 1) * (n - 1), 9)
    if k > 2 and k % 1 == 0: K += ["%s %d-gonal number" % (
      str(i) + 'tsnrhtdd'[i % 5 * (i % 100 ^ 15 > 4 > i % 10)::4], k
    )]
  return K or 0

