
def sum_numbers(n):
  if n == 1:
    return 1
  return n + sum_numbers(n-1)

