
def lcm_of_list(a):
  t=len(a)
  i,b,c=0,1,0
  while i<t-1:
    if a[i]>a[i+1]:
      a[i],a[i+1]=a[i+1],a[i]
    for j in range(2,a[i]+1):
        if a[i]%j==0 and a[i+1]%j==0:
          b=j
    a[i+1]=int(a[i]*a[i+1]/b)
    b=1
    i+=1
  return a[len(a)-1]

