
def reorder_digits(lst, strOne):
  new_lst = [];
  if strOne == 'asc':
    for i in lst: 
      new_lst.append(int("".join(sorted(str(i)))));
  elif strOne == 'desc':
    for i in lst: 
      new_lst.append(int("".join(sorted(str(i), reverse = True))));
  return new_lst;

