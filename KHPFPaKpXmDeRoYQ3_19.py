
def check_score(s):
  key = {'#': 5, 'O': 3, 'X': 1, 
    '!': -1, '!!': -3, '!!!': -5}
  return max(sum(key[i] for row in s for i in row), 0)

