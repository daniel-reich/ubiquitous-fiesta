
def check_sum(lst, n):
  for num in lst[:-1]:
    for next_num in lst[1:]:
      if num + next_num == n:
        return True
  return False

