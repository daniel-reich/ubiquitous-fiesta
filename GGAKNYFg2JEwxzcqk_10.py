
def anti_divisors(n):
  lst = []
  for x in range(1,n):
    if x>1 and x<n and n%x!=0:
      if x%2 and ((n * 2 - 1)%x==0 or (n * 2 + 1)%x==0):  lst.append(x)
      elif x%2==0 and (n * 2)%x==0: lst.append(x)
  return lst

