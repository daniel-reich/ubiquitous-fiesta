
def lines_are_parallel(l1, l2):
  if l1[0] == 0:
    if l2[0] == 0 and l1[1] == l2[1]:
      return True
    else:
      return False
  return(l1[1]/l1[0] == l2[1]/l2[0])

