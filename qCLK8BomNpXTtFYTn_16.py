
def cumulative_sum(lst):
  new_list = []
  sum = 0
  for num in lst:
    sum += num
    new_list.append(sum)
  return new_list

