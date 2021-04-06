
def possible_path(lst):
  for i, l in enumerate(lst):
    if i in range(1, len(lst)-1):
      if type(l) == int:
        if str(lst[i-1])+str(lst[i+1]) != "HH":
          return False
  return True

