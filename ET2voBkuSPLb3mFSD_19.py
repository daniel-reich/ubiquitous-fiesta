
def sum_every_nth(numbers, n):
  newlist = numbers[n-1::n]
  return sum(newlist)

