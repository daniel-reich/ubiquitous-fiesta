
def sum_every_nth(numbers, n):
  return sum(numbers[i-1] for i in range(1,len(numbers)+1) if not i%n)

