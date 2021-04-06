
def tf_lst(lst):
  if lst[0] != round(10 + 0.1*lst[4],1):
    return False
  if lst[1] != 2*lst[4]:
    return False
  if lst[2] + lst[4] != lst[5]:
    return False
  if lst[3] != 321*lst[4]:
    return False
  if lst[6] != lst[4]**2:
    return False
  if lst[7] != round(lst[4]*1.2,1):
    return False
  return True

