
def product(x):
  p=1
  for i in str(x):
    p*=int(i)
  return p  
def max_product(n):
  p=product(n)
  max=0
  for a in range(n,int(.6*n),-1):
    if product(a)>=max:
      max=product(a)
      n1=a
  if p>max:
    return [n]
  if '1' in str(n1):
    return [int(str(n1)[1:]),n1]
  else:
    return [n1]

