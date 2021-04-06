
def is_narcissistic(n):
  num_digits = len(str(n))
  total = 0
  for num in str(n):
    total += int(num)**num_digits
  return total == n

