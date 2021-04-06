
def sum_two_smallest_nums(lst):
  new_lst = sorted(lst)
  poslst = list(filter(lambda x: x > 0, new_lst))
  lstsum = poslst[0]+poslst[1]
  return lstsum

