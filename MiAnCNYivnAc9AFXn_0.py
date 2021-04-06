
def change_types(lst):
  for i, j in enumerate(lst):
    if type(j) is int and j % 2 == 0:
      lst[i] += 1
    elif type(j) is str:
      lst[i] = lst[i].capitalize() + '!'
    elif type(j) is bool:
      lst[i] = not lst[i]
  return lst

