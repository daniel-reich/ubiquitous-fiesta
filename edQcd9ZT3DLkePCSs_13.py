
def sum_first_n_nums(lst, n):
  if n > len(lst):
    return sum(lst)
  else:
    return sum(lst[0:n])

