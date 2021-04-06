
def trailing_zeros(n):
  if n > 0 and n%10==0:
    if n < 1000000:
      return (n-1)//4
    return (n-5)//4
  return n//4

