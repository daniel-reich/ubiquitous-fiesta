
def odds_vs_evens(num):
  odd = 0
  even = 0
  for i in str(num):
    if int(i) % 2 == 0:
      even += int(i)
    else:
      odd += int(i)
  if odd > even:
    return 'odd'
  elif even > odd:
    return 'even'
  else:
    return 'equal'

