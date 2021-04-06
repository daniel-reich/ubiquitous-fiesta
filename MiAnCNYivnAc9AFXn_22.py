
def change_types(lst):
  for k,el in enumerate(lst):
    if type(el) == bool:
      lst[k] = not lst[k]
    elif type(el) == str:
      lst[k] = lst[k].title() + '!'
    elif type(el) == int and el % 2 == 0:
      lst[k]+=1
    else:
      pass
  return lst

