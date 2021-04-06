
def remove_smallest(lst):
  ans = lst
  for i in lst:
    if i == min(lst):
      ans.remove(i)
      break
  return ans

