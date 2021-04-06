
def get_primiera_score(hand):
  dic = {'7': 21, '6': 18, 'A': 16, 'J': 10, 'Q': 10, 'K': 10}
  value = lambda x: dic[x[:-1]] if x[:-1] in dic else 10 + int(x[:-1])
  if all(s in str(hand) for s in 'dhsc'):
    return sum(max(value(c) for c in hand if c.endswith(s)) for s in 'dhsc')
  return 0

