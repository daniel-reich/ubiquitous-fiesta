
def sum_two_smallest_nums(lst):
  ordered = sorted(lst)
  new_lst = [i for i in ordered if i >= 0]
  return new_lst[0] + new_lst[1]

