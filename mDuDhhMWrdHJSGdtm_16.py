
def prima(x):
  for i in range (2,x+1):
    if x%i==0 and x !=i:
      return False
    elif x % i==0 and x==i:
      return True
def is_exactly_three(n):
  if n==1:
    return False
  elif n!=1:
    ni=pow(n,1/2)
    a=list(str(ni))
    b=a.index(".")
    c=a[b:]
    if len(c)==2:
      chekprima=prima(int(ni))
      if chekprima==True:
        return True
      elif chekprima==False:
        return False
    elif len(c)!=2:
      return False

