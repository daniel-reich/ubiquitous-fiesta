
def odds_vs_evens(num):
  num = str(num)
  odd = sum(int(i) for i in num if int(i)%2==1)
  even = sum(int(i) for i in num if int(i)%2==0)
  if odd == even : return 'equal'
  return 'odd' if odd > even else 'even'

