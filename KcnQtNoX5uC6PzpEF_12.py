
def check_sum(lst, n):
  for x in range(len(lst)-1):
    for y in range(x+1, len(lst)):
      if lst[x] + lst[y] == n:
        return True
  return False

