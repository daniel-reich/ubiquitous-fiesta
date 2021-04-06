
def sum_every_nth(numbers, n):
  sub = numbers[n - 1::n]
  return sum(sub)

