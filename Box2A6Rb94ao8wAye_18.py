
def leader(lst):
  new_lst = []
  for i, v in enumerate(lst):
    if v == max(lst[i:]):
      new_lst.append(v)
  return new_lst

