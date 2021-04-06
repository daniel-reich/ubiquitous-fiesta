
def check_sum(lst, n):
  return any((n-v) in lst[i+1:] for i, v in enumerate(lst[:-1]))

