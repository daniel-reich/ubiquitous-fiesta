
def is_untouchable(n):
  lst = []
  if n < 2:
    return 'Invalid Input'
  for i in range(2, n*n+1):
    if sum(divisors(i)) == n:
      lst += [i]
  return not lst or lst
  
def divisors(n):
  divs = {1}
  for i in range(2, int(n**0.5)+1):
    if not n%i:
      divs.add(i)
      divs.add(n//i)
  return divs

