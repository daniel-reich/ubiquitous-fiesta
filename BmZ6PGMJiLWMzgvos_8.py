
def is_special_array(lst):
  for x in range(len(lst)):
    if x % 2 == 0 and lst[x] % 2 != 0:
      return False
    elif x % 2 != 0 and lst[x] % 2 == 0:
      return False
    
  return True

