
def jazzify(lst):
  new_lst = []
  for i in lst:
    if '7' not in i:
      new_lst.append(i+'7')
    else:
      new_lst.append(i)
  return new_lst

