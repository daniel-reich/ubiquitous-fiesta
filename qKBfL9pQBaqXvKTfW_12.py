
def sum_of_slices(lst):
  saved_lst, new_lst = [], []
  for x in lst:
    if sum(new_lst) + x > 100:
      saved_lst.append(sum(new_lst))
      new_lst = []
    new_lst.append(x)
  saved_lst.append(sum(new_lst))
  return saved_lst

