
def repeating_cycle(n):
  if n%2==0 or n%5==0:
    return -1
  else:
    if n==1:
      return -1
    else:
      k=1
      while (10**k)%n!=1:
        k+=1
      return k

