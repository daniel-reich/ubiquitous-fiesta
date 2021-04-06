
def check_score(s):
  inst = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
  score = sum(sum(inst[i] for i in j) for j in s)
  return score*(score>0)

