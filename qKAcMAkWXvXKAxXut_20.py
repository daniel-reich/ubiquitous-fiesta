
def calc_bundled_temp(n, temp):
  t = float(temp.split("*")[0])
  for i in range(n):
    t*=1.1
  return str(round(t,1))+"*C"

