
def count_number(lst):
  sum_ = 0
  for i in range(len(lst)):
    if type(lst[i]) == list:
      sum_ += count_number(lst[i])
    elif type(lst[i]) == int or type(lst[i]) == float:
      sum_ += 1
  return sum_

