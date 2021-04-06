
def sum_every_nth(numbers, n):
  i = 1;
  sum = 0;
  for x in numbers:
    if i == n:
      sum = sum + x
      i = 0
    i = i + 1
  return sum

