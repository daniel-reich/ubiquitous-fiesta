
def max_collatz(n):
  m = n
  while n !=1:
    if n%2==0:
      n = n // 2
    else:
      n = (n*3) + 1
    if n > m: m = n
  return m

