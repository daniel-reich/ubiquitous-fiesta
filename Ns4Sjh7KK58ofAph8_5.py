
def is_triplet(n1, n2, n3):
  lst=[n1,n2,n3]
  lst.sort()
  return lst[0]*lst[0]+lst[1]*lst[1]==lst[2]*lst[2]

