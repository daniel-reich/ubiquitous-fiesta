
def in_box(lst):
  flag = False
  for item in lst[1:-1]:
    if '*' in item[1:-1]:
      flag = True
      break
  return flag

