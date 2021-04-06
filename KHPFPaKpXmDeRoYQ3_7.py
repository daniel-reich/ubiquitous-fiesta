
def check_score(s):
  values = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5 }
  total = sum(values[s[r][c]] for r in range(len(s)) for c in range(len(s[0])))
  return total if total > 0 else 0

