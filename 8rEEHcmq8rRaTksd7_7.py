
def lines_are_parallel(l1, l2):
  if l1[0]!=0 and l2[0]!=0:
    return l1[1]/l1[0] == l2[1]/l2[0]
  if l1[0]==0 and l2[0]!=0:
    return False
  return l1[1]==l2[1]

