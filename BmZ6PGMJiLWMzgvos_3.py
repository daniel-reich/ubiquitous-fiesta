
def is_special_array(lst):
  false = 0
  for num in lst[::2]:
    if num % 2 != 0:
      false += 1
  if false != 0:
    return False
  else:
    for num in lst[1::2]:
      if num % 2 == 0:
        false += 1
  if false != 0:
    return False
  return True

