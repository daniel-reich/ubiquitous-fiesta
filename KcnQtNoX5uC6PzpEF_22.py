
def check_sum(lst, n):
  return any(a + b == n for a in lst for b in lst)

