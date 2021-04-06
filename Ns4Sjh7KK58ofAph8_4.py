
def is_triplet(n1, n2, n3):
  list=[n1,n2,n3]
  x=sorted(list)
  if ((x[0])**2) + (x[1])**2==x[2]**2:
    return True
  else:
    return False

