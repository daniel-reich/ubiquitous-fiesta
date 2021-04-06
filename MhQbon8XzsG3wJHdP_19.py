
def solve_for_exp(a, b):
  x = 1
  while a ** x != b:
    x += 1
  return x

