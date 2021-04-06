
def is_untouchable(n):
  if n < 2:
    return "Invalid Input"
  return [k for k in range(2, n*n + 1) if sum(divs(k)) == n-1] or True
  
def divs(n):
  i = 2
  while i*i < n:
    if n % i == 0:
      yield i
      yield n // i
    i += 1
  if i*i == n:
    yield i

