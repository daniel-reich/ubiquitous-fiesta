
def change_types(lst):
  for i, val in enumerate(lst):
    if isinstance(val, str):
      val = val + "!"
      val = val.capitalize()
    elif isinstance(val, bool):
      val = not val
    elif val %2 == 0:
      val += 1
    lst[i] = val
  return lst

