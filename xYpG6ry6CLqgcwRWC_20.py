
def sum_two_smallest_nums(lst):
  new_lst = []
  for num in lst:
    if num > 0:
      new_lst.append(num)
  new_lst_1 = sorted(new_lst)
  return new_lst_1[0] + new_lst_1[1]

