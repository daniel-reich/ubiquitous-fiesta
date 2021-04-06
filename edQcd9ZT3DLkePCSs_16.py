
def sum_first_n_nums(lst, n):
  su = 0
  if n >= len(lst):
    su = sum(lst)
    return su
  elif n == 0:
    return su
  else:
    i = len(lst) - n
    su = sum(lst[0: i + 1])
    return su

