
def portion_happy(l):
  z=lambda z:sum(l[i]in[l[i-1],l[i+1]]for i in range(1,len(l)-1)if l[i]==z)
  l=[1-l[0]]+l+[1-l[-1]]
  return (z(0)+z(1))/(len(l)-2)

