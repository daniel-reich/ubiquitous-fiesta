
def validate_swaps(lst, txt):
  res = []
  for l in lst:
    if len(l) == len(txt):
      cnt = 0
      for i,c in enumerate(l):
        if c != txt[i]:
          cnt += 1
      res.append(cnt == 2)
    else:
      res.append(False)
  return res

