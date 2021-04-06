
def in_box(lst):
  for i in lst:
    for x in i:
      if i.index(x) > 0 and i.index(x) < len(i)-1:
        if x in '*':
          return True
  return False

