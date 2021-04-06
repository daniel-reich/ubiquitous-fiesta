
def changeTypes(lst):
  for i, item in enumerate(lst):
    if type(lst[i]) == str:
      lst[i] = lst[i].capitalize() + '!'
    elif type(lst[i]) == int:
      if lst[i]%2 == 0:
        lst[i] += 1
    else:
      lst[i] = not (lst[i] or False)
  return lst

