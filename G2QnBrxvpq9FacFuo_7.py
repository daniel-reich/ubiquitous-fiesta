
def possible_path(lst):
  for i in range(len(lst)-1):
    if type(lst[i]) == int:
      if type(lst[i+1]) == int:
        return False
  return True

