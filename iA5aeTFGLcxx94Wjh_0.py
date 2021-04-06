
def delete_occurrences(lst, num):
  new_lst = []
  for i in lst:
    if new_lst.count(i) < num:
      new_lst.append(i)
  return new_lst

