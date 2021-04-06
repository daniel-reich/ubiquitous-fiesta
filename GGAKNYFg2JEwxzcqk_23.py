
def anti_divisors(n):
  adl = list(range(1,n))
  divlst = []
  for i in adl:
    if n%i!=0:
      if i%2!=0:
        if (n*2-1)%i==0 or (n*2+1)%i==0:
          divlst.append(i)
      elif i%2==0:
        if (n*2)%i==0:
          divlst.append(i)
  return divlst

