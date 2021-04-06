
def simplify_sqrt(n):
  a=[]
  k=n
  x=1
  y=1
  i=2
  while i <= k:
    if k%i==0:
      a=a+[i]
      k=k/i
      i=i-1
    i=i+1
  # a = prime factors of n
  i=0
  while i < len(a):
    try:
      if a[i]==a[i+1]:
        x=x*a[i]
        i=i+1
      else: 
        y=y*a[i]
    except:
      y=y*a[i]
    i=i+1
  return (x,y)

