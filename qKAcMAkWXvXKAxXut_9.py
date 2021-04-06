
def calc_bundled_temp(n, t):
  v = int(t[:-2])
  for i in range(n): v *= 1.1 
  return '{:.1f}*C'.format(v)

