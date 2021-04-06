
def calc_bundled_temp(n, temp):
  i = int(temp[:-2])
  for x in range(n):
    i *= 1.1
  return str(round(i,1)) + "*C"

