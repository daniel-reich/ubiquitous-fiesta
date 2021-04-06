
def prime_factorization(n):
  ans=[]
  while n%2==0:
    ans.append(2)
    n=n//2
  for i in range(3,n+1,2):
    if n%i==0:
      ans.append(i)
      n=n//i
  if n>2:ans.append(n)
  return sorted(ans)

