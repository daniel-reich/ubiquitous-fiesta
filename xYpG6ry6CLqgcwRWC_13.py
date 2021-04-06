
def sum_two_smallest_nums(lst):
  out_lst = []
  for i in lst:
    if i >= 0:
      out_lst.append(i)
  out_lst.sort()
  out_val = out_lst[0] + out_lst[1]
  return out_val

