
def odds_vs_evens(num):
  s1 = 0
  s2 = 0
  for ch in str(num):
    if int(ch)%2 ==0:
      s1 += int(ch)
    else:
      s2 += int(ch)
  if s1>s2:
    return 'even'
  if s2>s1:
    return 'odd'
  return 'equal'

