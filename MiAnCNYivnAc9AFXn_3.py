
def change_types(lst):
  for i, x in enumerate(lst):
    if type(x) == int: lst[i] += (lst[i] + 1) % 2
    elif type(x) == str: lst[i] = lst[i].capitalize() + "!"
    elif type(x) == bool: lst[i] =  not lst[i]
  return lst

