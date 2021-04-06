
def is_narcissistic(n):
  y = len(str(n))
  total = 0
  for i in str(n):
    total += (int(i))**y
  return total == n

