
def is_positive_dominant(lst):
  count = 0
  arr = set(lst)
  for x in arr:
    if x > 0:
      count += 1
    elif x < 0:
      count -= 1
    else:
      pass
  if count > 0:
    return True
  else:
    return False

