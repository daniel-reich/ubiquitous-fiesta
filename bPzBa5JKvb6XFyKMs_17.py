
def get_primiera_score(deck):
  d =   { '7': 21,'6': 18,'A': 16,'5': 15,'4': 14,
      '3': 13,'2': 12,'K': 10,'Q': 10,'J': 10 }
  sdeck = [[d[x[0]] for x in deck if x[1] == y] for y in 'dhcs']
  return sum(max(x) for x in sdeck) if all(x for x in sdeck) else 0

