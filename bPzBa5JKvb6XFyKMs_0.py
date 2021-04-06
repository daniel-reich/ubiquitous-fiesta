
def get_primiera_score(deck):
  d = {"7":21, "6":18, "A":16, "J":10, "Q":10, "K":10}
  for k in range(2, 6):
    d[str(k)] = 10 + k
  if len(set([k[1] for k in deck])) != 4:
    return 0
  return sum([max([d[j[0]] for j in deck if j[1] == i]) for i in 'chds'])

