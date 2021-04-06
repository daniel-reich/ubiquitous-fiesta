
def quad_sequence(lst):
  x=len(lst)
  a=(lst[0]-2*lst[1]+lst[2])/2
  b=lst[1]-lst[0]-3*a
  c=lst[0]-a-b
  S=[]
  for i in range(x+1,2*x+1):
    S.append(a*(i**2)+b*i+c)
  return S

