
def is_special_array(lst):
  for i in range(len(lst)):
    if i % 2 != lst[i] % 2:
      return False
  return True

