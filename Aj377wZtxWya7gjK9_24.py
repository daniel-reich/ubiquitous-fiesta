
def sum_missing_numbers(lst):
  list_sum = sum(lst)
  max_val = max(lst)
  min_val = min(lst)
  consecutives_sum = sum([i for i in range(min_val,max_val + 1)])
  return consecutives_sum - list_sum

