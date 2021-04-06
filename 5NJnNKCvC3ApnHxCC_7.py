
def mubashir_function(a, b):
  sta = str(a)
  stb = str(b)
  anum = 0
  bnum = 0
  for x in sta:
    anum += int(x)
  for y in stb:
    bnum += int(y)
  return anum * bnum

