
def sum_numbers(n):
  if n == 1:
    return n
  else:
    return n + sum_numbers(n - 1)

