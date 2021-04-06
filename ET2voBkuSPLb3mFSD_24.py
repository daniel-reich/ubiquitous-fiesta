
def sum_every_nth(numbers, n):
  numbers.insert(0,0)
  return sum(numbers[::n])

