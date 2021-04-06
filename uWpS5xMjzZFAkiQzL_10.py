
def odds_vs_evens(num):
  od, ev = 0, 0
  for x in str(num):
    if int(x) % 2 == 0:
      ev += int(x)
    else:
      od += int(x)
  if od > ev:
    return 'odd'
  elif od < ev:
    return 'even'
  else:
    return 'equal'

