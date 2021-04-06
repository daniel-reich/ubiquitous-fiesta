
def is_special_array(lst):
  for y,x in enumerate(lst):
    if(x % 2 == 0 and y % 2 != 0):return False
    if(x % 2 != 0 and y % 2 == 0):return False
  return True

