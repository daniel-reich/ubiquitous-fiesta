
def completely_filled(lst):
  for x in lst:
    if ' ' in x:
      return False
    else:
      continue
  return True

