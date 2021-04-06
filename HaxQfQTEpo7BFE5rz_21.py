
def alternate_pos_neg(lst):
  if len(lst) == 1 and lst[0] == 0:
    return False
  else:
    counter1 = 0
    for i in range(len(lst)-1):
      if (lst[i] >= 0 and lst[i+1] < 0) or (lst[i+1] > 0 and lst[i] < 0):
        counter1 += 1
      else:
        return False
    if counter1 == len(lst)-1:
      return True
    return False

