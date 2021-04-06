
def trailing_zeros(n):
  ans = 0
  
  while n>= 5:
    n //= 5
    ans += n
  
  return ans

