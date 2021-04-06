
def is_special_array(lst):
  for x in range(len(lst)):
    if x%2 == 0 and lst[x]%2 == 0:
      continue
    elif x%2 != 0 and lst[x]%2 != 0:
      continue
    else:
      return False
  return True

