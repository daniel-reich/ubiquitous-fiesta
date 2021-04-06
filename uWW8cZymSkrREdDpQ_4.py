
def sums_up(lst):
  ans = []
  for i,n in enumerate(lst[::-1]):
    if 8-n in lst[::-1][i+1:]:
      ans.append(sorted([n,8-n]))
  return {"pairs": ans[::-1]}

