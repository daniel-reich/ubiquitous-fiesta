
def check_score(s):
  vals = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
  ans = sum(sum(vals[sym] for sym in line) for line in s)
  return max(ans,0)

