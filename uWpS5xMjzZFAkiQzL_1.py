
def odds_vs_evens(num):
  even = sum(int(i) for i in str(num) if int(i) % 2 == 0)
  odd = sum(int(i) for i in str(num) if int(i) % 2 != 0)
  return 'odd' if odd > even else 'even' if even > odd else 'equal'

