
def alternate_pos_neg(lst):
  if 0 in lst: return False
  return all(lst[i]*lst[i+1]<0 for i in range(len(lst)-1))

