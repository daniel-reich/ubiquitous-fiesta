
def find_odd(lst):
  ans = 0
  for i in lst:
    ans^=i
  return ans

