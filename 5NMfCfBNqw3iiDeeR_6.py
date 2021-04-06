
def sum_minimums(lst):
  min_num = []
  for num_lst in lst:
    min_num.append(min(num_lst))
  return sum(min_num)

