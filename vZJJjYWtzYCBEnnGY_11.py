
def briscola_score(d1, d2):
  v = {'A':11,'3':10,'K':4,'Q':3,'J':2}
  d1 = sum(v[i[:-1]] if i[:-1] in 'A3KQJ' else 0 for i in d1)
  d2 = sum(v[i[:-1]] if i[:-1] in 'A3KQJ' else 0 for i in d2)
  return 'You Win!' if d1+d2 > 120 else 'You Lose!' if d1+d2 < 120 else 'Draw!'

