
def calc_bundled_temp(n, temp):
  t = int(temp[0:-2])
  mul = 1.1**n
  res = round(mul*t, 1)
  return str(res) + "*C"

