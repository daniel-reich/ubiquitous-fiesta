
def completely_filled(lst):
  for i in lst:
    if ' ' in i:
      return False
  return True

