
def is_shifted(l1, l2):
  if len(l1) != len(l2): return False
  return all(l1[i]+l2[i-1]==l1[i-1]+l2[i] for i in range(1,len(l1)))
  
def is_multiplied(l1, l2):
  if len(l1) != len(l2): return False
  return all(l1[i]*l2[i-1]==l1[i-1]*l2[i] for i in range(1,len(l1)))

