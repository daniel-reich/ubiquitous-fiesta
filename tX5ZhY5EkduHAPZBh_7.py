
def nearest_element(n, l):
  a=sorted(l,key=lambda x:abs(n-x))
  d=abs(n-a[0])
  a=[i for i in a if abs(n-i)==d]
  return l.index(max(a))

