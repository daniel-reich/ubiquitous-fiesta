
def mystery_func(num):
  l=[]
  for i in range(1,num):
    if(pow(2,i)<=num):
      l.append(i)
  m=max(l)
  r=num-pow(2,m)
  a='2'*m+str(r)
  return int(a)

