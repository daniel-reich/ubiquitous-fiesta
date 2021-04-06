
def in_box(lst):
  for x in lst:
    if '*' in x:
      return True
  return False

