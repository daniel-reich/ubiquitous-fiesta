
def not_good_math(n,k):
  for i in range(k):
    n=n-1 if n%10 else n//10
  
  return n

