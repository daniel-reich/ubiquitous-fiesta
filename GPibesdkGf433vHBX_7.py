
def is_prime(n):
  for i in range(2,n):
    if n%i==0:return False
  return True
def goldbach_conjecture(n):
  ans=[]
  if n<2 or n%2: return ans
  for i in range(2,n):
    if is_prime(i):
      if is_prime(n-i):
        ans.append(i)
        ans.append(n-i)
        return ans

