
def in_box(lst):
  counter = 0
  if '*' in lst[0] or '*' in lst[-1]:
    return False
  else:
    for i in lst[1: len(lst) - 1]:
      if '*' in i:
        counter += 1
    return counter >= 1

