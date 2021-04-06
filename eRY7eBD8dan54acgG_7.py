
def is_checkerboard(lst):
  for x,y in zip(lst,lst[1:]):
    if any(q==t for q,t in zip(x,y)):
      return False
  return True

