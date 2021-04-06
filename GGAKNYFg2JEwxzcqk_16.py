
def anti_divisors(n):
  lst = []
  for i in range (2,n):
    if n%i == 0:
      continue
    if i%2==0:
      if (n*2)%i==0:
        lst.append(i)
    else:
      if (n*2+1)%i==0 or (n*2-1)%i==0:
        lst.append(i)
  
  return lst

