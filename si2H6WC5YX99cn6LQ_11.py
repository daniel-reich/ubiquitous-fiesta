
def sum_numbers(n):
  return n + sum_numbers(n-1) if not n == 1 else 1

