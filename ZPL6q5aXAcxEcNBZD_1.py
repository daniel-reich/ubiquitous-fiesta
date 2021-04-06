
def funny_numbers(n, p):
  sp = sum(int(c)**(p+i) for i, c in enumerate(str(n)))
  return sp//n if sp%n == 0 else None

