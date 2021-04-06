
def kempner(n):
  kempVal = 1
  factorial = 1 % n
  while factorial != 0:
    kempVal += 1
    factorial = (factorial * kempVal) % n
  return kempVal

