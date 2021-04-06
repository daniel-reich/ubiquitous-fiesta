
def unique_lst(lst):
  if lst == []:
    return []
  ans = []
  for item in lst:
    if item > 0 and item not in ans:
      ans.append(item)
  return ans

