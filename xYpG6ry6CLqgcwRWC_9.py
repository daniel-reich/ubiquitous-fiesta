
def sum_two_smallest_nums(lst):
  sum_list = []
  for num in lst:
    if num > 0:
      sum_list.append(num)
  
  sum_list = sorted(sum_list)
  
  return (sum_list[0] + sum_list[1])

