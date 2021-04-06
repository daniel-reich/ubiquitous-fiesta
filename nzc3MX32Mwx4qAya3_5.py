
def ranged_reversal(lst, start, finish):
  newlst = []
  rev = []
  for i in range(len(lst)):
    if i in range(start, finish + 1):
      rev.append(lst[i])
    else:
      newlst.append(lst[i])
  for i in range(len(rev)):
    newlst.insert(start, rev[i])
  return (newlst)

