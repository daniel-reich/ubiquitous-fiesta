
def recaman(n,a=[0],d=[]):
  if n==0:a=[]
  i=len(a)
  while n>len(a):
    b=a[i-1]-i
    if b>0 and not b in a: a+=[b]
    else:
      b=a[i-1]+i
      if b in a and not b in d: d+=[b]
      a+=[b]
    i+=1
  return "---> Recaman's sequence: " + str(a) + "\n" + "---> Duplicates for n = " + str(n) + ": " + str(d)

