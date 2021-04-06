
def check_sum(lst, n):
  for i in range(len(lst)):
    for j in lst[:i]+lst[i:]:
      if lst[i]+j==n: return True
  return False

