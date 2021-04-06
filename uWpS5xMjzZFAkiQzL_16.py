
def odds_vs_evens(num):
  odd = sum([int(i) for i in str(num) if int(i) % 2 == 1])
  even = sum([int(i) for i in str(num) if int(i) % 2 == 0])
  
  if odd == even:
    return 'equal'
  elif odd > even:
    return 'odd'
  elif even > odd:
    return 'even'

