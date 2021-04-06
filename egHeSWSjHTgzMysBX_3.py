
def half_a_fraction(f):
  a, b = list(map(int, f.split("/")))
  if a % 2 == 0:
    a //= 2
  else:
    b *= 2
  return str(a) + "/" + str(b)

