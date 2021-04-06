
def check_sum(lst, n):
  for i in range(len(lst)):
    for j in range(i+1):
      if lst[i]+lst[j]==n:
        return True
  return False

