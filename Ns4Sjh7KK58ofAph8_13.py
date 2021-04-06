
def is_triplet(n1, n2, n3):
  x=[n1,n2,n3]
  lst=sorted(x)
  return lst[0]**2+lst[1]**2==lst[2]**2

