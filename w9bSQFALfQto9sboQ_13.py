
def gcd(n1, n2):
  lst=[]
  for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
      lst.append(i)
  return max(lst)

