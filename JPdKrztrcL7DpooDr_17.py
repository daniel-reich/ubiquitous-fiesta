
def collatz(n):
  ls=[]
  cnt=0
  if n==1:
    return [0,1]
  else:
    while n!=1:
      if n%2==0:
        n=n//2
        ls.append(n)
        cnt+=1
      else:
        n= (3*n)+1
        ls.append(n)
        cnt+=1
    l=sorted(ls)
    return [cnt,l[len(l)-1]]

