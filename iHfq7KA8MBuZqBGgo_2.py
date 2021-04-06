
def is_legitimate(lst):
  if lst[0].count(1) == 0 and lst[-1].count(1) == 0:
    for i in lst:
      if 1 == i[0] or i[-1]:
        return False
    return True
  return False

