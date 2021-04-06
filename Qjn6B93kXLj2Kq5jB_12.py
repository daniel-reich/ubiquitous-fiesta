
def simplify_frac(f):
  new=""
  f=f.split("/")
  n=0
  for i in range(1,int(f[0])+1):
    for j in range(1,int(f[1])+1):
      if int(f[0])%i==0 and int(f[1])%j==0:
        if i==j:
          n=i
  f[0]=int(f[0])//n
  f[1]=int(f[1])//n
  new=str(f[0])+"/"+str(f[1])
  return new

