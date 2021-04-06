
def find_factors(n):
  ans = []
  if n < 0:
    return [] 
  for i in range(1,n+1):
    if n % i == 0:
      ans.append(i)
  return ans

