
def unique_lst(lst):
  new_lst = []
  for num in lst:
    if num > 0 and num not in new_lst:
      new_lst.append(num)
  return new_lst

