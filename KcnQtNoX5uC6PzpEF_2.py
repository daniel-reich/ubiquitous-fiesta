
def check_sum(lst, n):
  for i, n1 in enumerate(lst):
    for n2 in lst[i + 1:]:
      if n1 + n2 == n:
        return True
  return False

