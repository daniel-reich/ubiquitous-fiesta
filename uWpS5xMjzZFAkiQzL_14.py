
def odds_vs_evens(num):
  odd = []
  even = []
  for i in str(num):
    if int(i) %2 == 0:
      even.append(int(i))
    else:
      odd.append(int(i))
  if sum(odd) > sum(even):
    return 'odd'
  elif sum(even) > sum(odd):
      return 'even'
  else:
    return 'equal'

