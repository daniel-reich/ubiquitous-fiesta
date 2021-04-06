
def daily_streak(lst):
  tmp = 0
  res = 0
  for b in lst:
    if b == True:
      tmp += 1
    else:
      res = max(tmp,res)
      tmp = 0
  res = max(tmp,res)
  return res

