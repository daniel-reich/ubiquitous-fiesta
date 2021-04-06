
def check_sum(lst, n):
  for i in lst:
    d = n - i
    if d in lst: return True
  return False

