
def divisible_by_b(a, b):
  res = int (a / b)
  while res * b < a:
    res += 1
  return res * b

