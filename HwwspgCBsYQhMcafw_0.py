
def super_digit(n, k):
  return sum(map(int, n)) * k % 9 or 9

