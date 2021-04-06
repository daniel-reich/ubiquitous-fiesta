
def sum_numbers(n):
  if not n: return 0
  return n + sum_numbers(n-1)

