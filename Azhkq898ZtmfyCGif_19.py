
def replace_list(first, last, ans):
  if first != last:
    ans.append(str(first) + '-' + str(last))
  else:
    ans.append(str(first))
  return ans
​
def numbers_to_ranges(lst):
  if len(lst) == 0: return []
  first = lst[0]
  last = lst[0]
  ans = []
  for i in range(len(lst) - 1):
    if lst[i] + 1 == lst[i+1]:
      last = lst[i+1]
    else:
      ans = replace_list(first, last, ans)
      first = lst[i+1]
  ans = replace_list(first, last, ans)
  return ans

