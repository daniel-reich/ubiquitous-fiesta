
def change_types(lst):
  res = []
  for i in lst:
    if type(i) == int:
      res.append(i if i%2 else i+1)
    elif type(i) == str:
      res.append(i.title() + '!')
    else:
      res.append(not i)
  return res

