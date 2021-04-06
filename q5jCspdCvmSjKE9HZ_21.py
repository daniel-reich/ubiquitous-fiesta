
def lcm_of_list(numbers):
  x=max(numbers)
  e=""
  x=max(numbers)
  r=[]
  b=[]
  for n in numbers:
    if n%2==0:
      b.append(n)
    else:
      r.append(n)
  t=max(r)
  z=max(b)
  a=list(numbers)
  for n in numbers:
    if n==1:
      a.remove(1)
    elif n==t or n==z:
      continue
    elif t%n==0:
      a.remove(n)
    elif z%n==0:
      a.remove(n)
  switch=True
  while(True):
    for i in a:
      if x%i!=0:
        switch=False
        break
      elif x%i==0:
        continue
    if switch==True:
      return x
    else:
      x+=max(numbers)
      switch=True

