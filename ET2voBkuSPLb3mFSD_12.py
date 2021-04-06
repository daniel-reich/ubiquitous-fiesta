
def sum_every_nth(numbers, n):
  return sum([numbers[x-1] for x in range(0,len(numbers)+1,n) if x-1>=0])

