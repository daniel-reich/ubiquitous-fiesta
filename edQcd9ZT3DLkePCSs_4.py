
def sum_first_n_nums(lst, n):
  sum = 0
  i = 0;
  while i < n and i < len(lst):
    sum += lst[i]
    i += 1
  return sum

