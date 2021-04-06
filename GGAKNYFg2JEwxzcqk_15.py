
def anti_divisors(n):
  ret = []
  for i in range(1,n+1):
    if n%i!=0:
      if i%2!=0:
        if (n*2-1)%i==0 or (n*2+1)%i==0:
          ret.append(i)
      else:
        if (n*2)%i==0:
          ret.append(i)
  return ret

