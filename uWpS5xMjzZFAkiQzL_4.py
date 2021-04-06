
def odds_vs_evens(num):
  num = str(num)
  lis1 =[int(i) for i in num if int(i) % 2 == 0]
  lis2 =[int(i) for i in num if int(i) % 2 != 0]
  if sum(lis1) > sum(lis2):
    return 'even'
  elif sum(lis1) < sum(lis2):
    return 'odd'
  else:
    return 'equal'

