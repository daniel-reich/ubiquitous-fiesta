
def recaman(n):
  l,d,k=[],[],0
  for x in range(n):
    k-=x
    if k in l or k<0:
        k+=x+x
        if k not in d and k in l:d.append(k)
    l.append(k)
  return"---> Recaman's sequence: %s\n---> Duplicates for n = %s: %s"%(l,n,d)

