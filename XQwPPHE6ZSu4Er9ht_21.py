
def prime_factors(num):
  output=[]
  for i in range(2,num):
    while(num%i==0):
      output.append(i)
      num=int(num/i)
  return output
def is_economical(m):
  l=prime_factors(m)
  d={}
  for n in l:
    if(n in d):
      d[n]+=1
    else:
      d[n]=1
  c=0
  for elt in d:
    if(d[elt]==1):
      c=c+len(str(elt))
    else:
      c=len(str(elt))+len(str(d[elt]))+c
  if(c==0):
    c=1
  if(len(str(m))==c):
    return "Equidigital"
  elif(len(str(m))>c):
    return "Frugal"
  else:
    return "Wasteful"

