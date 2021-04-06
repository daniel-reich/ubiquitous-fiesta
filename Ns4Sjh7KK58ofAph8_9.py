
def is_triplet(n1, n2, n3):
  
  a=[n1,n2,n3]
  a.sort()
  
  s=a[0]
  m=a[1]
  l=a[2]
  
  if (s**2+m**2)==l**2:
    return True
  else :
    return False

