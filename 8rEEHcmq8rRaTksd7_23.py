
def lines_are_parallel(l1, l2):
  if l1[0]!=0 and l2[0]!=0:
    if l1[1]/l1[0]==l2[1]/l2[0]:
      return True
    elif l1[1]/l1[0]!=l2[1]/l2[0]:
      return False
  elif l1[0]==0 and l2[0]==0:
    if l1[1] == l2[1]:
      return True
    elif l1[1] != l2[1]:
      return False

