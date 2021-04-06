
def is_factorial(n):
  factorials = [1]
  for i in range(2, n):
    factorials.append(factorials[-1]*i)
  return n in factorials

