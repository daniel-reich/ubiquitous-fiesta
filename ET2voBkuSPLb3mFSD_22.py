
def sum_every_nth(numbers, n):
  return sum([numbers[i] for i in range(n - 1, len(numbers), n)])

