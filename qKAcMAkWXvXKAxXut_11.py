
def calc_bundled_temp(n, temp):
  T = int(temp.rstrip("*C"))
  while n:
    T += T / 10
    n -= 1
  return str(round(T, 1)) + "*C"

