
def sum_every_nth(numbers, n):
  sum = 0
  for idx, num in enumerate(numbers, 1):
    if idx % n == 0:
      sum += num
  return sum

