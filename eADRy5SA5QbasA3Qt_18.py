
def sum_digits(n):
  n = str(n)
  total = 0
  for i in n:
    total += int(i)
  return total
​
def is_harshad(n):
  return n % sum_digits(n) == 0

