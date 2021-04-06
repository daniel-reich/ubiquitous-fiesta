
def daily_streak(lst):
  c = 0
  max_ = 0
  for b in lst:
    if b:
      c += 1
    else:
      max_ = c
      c = 0
  return max(c, max_)

