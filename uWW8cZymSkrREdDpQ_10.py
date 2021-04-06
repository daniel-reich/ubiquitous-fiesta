
def sums_up(lst):
  a=[[i,j] for i in lst for j in lst if i+j==8 and i<j]
  l=lambda y: lst.index(y)
  s=lambda x: min(l(x[0]),l(x[1]))+abs(l(x[0])-l(x[1]))
  return {'pairs':sorted(a,key=s)}

