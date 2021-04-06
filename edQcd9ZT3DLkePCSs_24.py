
def sum_first_n_nums(lst, n):
  if n>len(lst):
    return sum(lst)
  else:
    s=0
    for i in range(n):
      s=s+lst[i]
    return s

