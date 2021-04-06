
def match_last_item(lst):
  ans = []
  for x in range(len(lst)):
    if lst[x] != lst[-1]:
      ans.append(str(lst[x]))
  return ''.join(ans) == lst[-1]

