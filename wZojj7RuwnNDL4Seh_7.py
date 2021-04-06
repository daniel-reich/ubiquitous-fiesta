
def completely_filled(lst):
  for row in lst:
    if row.count(" ") > 0:
      return False
  return True

