
def get_primiera_score(deck):
  cards = {'s':[], 'h':[], 'd':[], 'c':[]}
  for s,c in [(cd[1], cd[0]) for cd in deck]:
    cards[s].append(c)
  if any(not lst for lst in cards.values()):
    return 0
  return sum(max(map(primiera, lst)) for lst in cards.values())
  
def primiera(cd):
  if cd in 'JQK': return 10
  if cd in '2345': return int(cd) + 10
  if cd == 'A': return 16
  if cd == '6': return 18
  if cd == '7': return 21
  return 0

