
def sums_up(lst):
  ret = {"pairs":[]}
  for i in range(len(lst)):
    for j in range(i):
      if lst[i]+lst[j]==8:
        ret["pairs"].append(sorted([lst[i],lst[j]]))
  return ret

