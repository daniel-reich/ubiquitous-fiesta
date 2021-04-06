
def odds_vs_evens(num):
  lst = [int(n) for n in str(num)]
  s_odds = sum(i for i in lst if i%2)
  s_evens = sum (i for i in lst if not i%2)
  return 'odd' if s_odds > s_evens else 'even' if s_evens > s_odds else 'equal'

