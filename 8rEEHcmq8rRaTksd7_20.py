
def lines_are_parallel(l1, l2):
  m1 = (-l1[0]/l1[1])
  m2 = (-l2[0]/l2[1])
  if m1 == m2:
      return True 
  else:
      return False

