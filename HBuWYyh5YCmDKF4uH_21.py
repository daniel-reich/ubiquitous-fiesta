
def almost_sorted(lst):
  inc = 0
  dec = 0
  for i, j in zip(lst, lst[1:]):
    if i < j:
      inc += 1
    else:
      dec += 1
  
  if (inc == 1) or (dec == 1):
    return True
  return False

