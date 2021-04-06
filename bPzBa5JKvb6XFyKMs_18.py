
def points(card):
  card=card[0]
  if card.isalpha(): return 10+6*(card=='A')
  if card<'6': return int(card)+10
  return 18+3*(card=='7')
​
def get_primiera_score(deck):
  if len(set([i[1] for i in deck]))!=4: return 0
  d={'h': [], 's': [], 'c': [], 'd': []}
  for i in deck: d[i[1]].append(points(i))
  return sum([max(d[i]) for i in d])

