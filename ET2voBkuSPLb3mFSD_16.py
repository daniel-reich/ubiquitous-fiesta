
def sum_every_nth(numbers, n):
  return sum(numbers[i-1] for i in range(n, len(numbers)+1, n))

