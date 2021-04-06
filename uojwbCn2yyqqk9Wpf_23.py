
def strict_divisors(n):
  """ Return a list with the strict_divisors or n """
  ### Function needed for is_untouchable()
  yield 1
  i = 2
  while i < n//i:
    if not n%i:
      yield i
      yield n//i
    i+=1
  if i**2==n: yield i
​
def is_untouchable(n):                    # Untouchable numbers
  """ Return if n if untouchable or not """
  results = []
  for x in range(2, n*n+1):
    if sum(list(strict_divisors(x)))==n: results.append(x)
  return "Invalid Input" if n<=1 else results if results else True

