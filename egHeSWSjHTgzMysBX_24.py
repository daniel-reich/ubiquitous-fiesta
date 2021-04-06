
def half_a_fraction(f):
  f = f.split('/')
  f[0] = int(f[0])
  f[1] = int(f[1])
  if f[0] % 2 == 1:
    f[1] = f[1] * 2
  else:
    f[0] = f[0] / 2
  f[0] = str(int(f[0]))
  f[1] = str(int(f[1]))
  return '/'.join(f)

