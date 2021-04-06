
def digits(n):
  d = len(str(n))
  ans = (n - 10**(d-1))*d #Digits with length d
  for x in range(1,d): #Digits with length d-1, d-2, etc.
    ans += (10**x - 10**(x-1))*x
    
  return ans

