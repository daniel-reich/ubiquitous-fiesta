
def alternate_pos_neg(lst):
  if 0 in lst:
    return False
  if lst[0] > 0: # List starts with positive number
    for num in range(len(lst)):
      if num % 2 == 0: # Positive index
        if lst[num] < 0:
          return False
      if num % 2 != 0: # Negative index
        if lst[num] > 0:
          return False
    return True
  if lst[0] < 0: # List starts with negative number
    for num in range(len(lst)):
      if num % 2 == 0: # Positive index
        if lst[num] > 0:
          return False
      if num % 2 != 0: # Negative index
        if lst[num] < 0:
          return False
    return True

