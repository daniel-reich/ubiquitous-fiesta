
def change_types(lst):
  nl = []
  for item in lst:
    if type(item) == int:
      if item % 2 == 0:
        nl.append(item + 1)
      else:
        nl.append(item)
    elif type(item) == str:
      nl.append(item.capitalize() + "!")
    elif type(item) == bool:
      nl.append(not item)
  return nl

