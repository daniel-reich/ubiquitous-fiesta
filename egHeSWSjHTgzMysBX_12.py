
def half_a_fraction(fract):
  f = fract.split("/")
  if int(f[0]) % 2 == 0:
    return str(int(f[0]) // 2) + "/" + f[1]
  else:
    return f[0] + "/" + str(int(f[1]) * 2)

