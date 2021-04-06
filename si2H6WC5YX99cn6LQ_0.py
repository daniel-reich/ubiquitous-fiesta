
def sum_numbers(n):
  return n + sum_numbers(n-1) if n else 0

