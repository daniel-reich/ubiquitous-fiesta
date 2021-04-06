
def divisible_by_b(a, b):
  return min(i for i in range(a, a + b + 1) if i % b == 0)

